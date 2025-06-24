import os
import cv2
import numpy as np
import re

INPUT_FOLDER = 'input-images'
OUTPUT_FOLDER = 'output-images'

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def align_and_overlay(rgb_img, thermal_img, pair_id):
    # Resize thermal image to match RGB dimensions
    thermal_img = cv2.resize(thermal_img, (rgb_img.shape[1], rgb_img.shape[0]))

    # Convert to grayscale
    gray_rgb = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
    gray_thermal = cv2.cvtColor(thermal_img, cv2.COLOR_BGR2GRAY)

    # CLAHE to enhance contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray_rgb = clahe.apply(gray_rgb)
    gray_thermal = clahe.apply(gray_thermal)

    # SIFT keypoints
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray_thermal, None)
    kp2, des2 = sift.detectAndCompute(gray_rgb, None)

    if des1 is None or des2 is None:
        print(f"[!] Descriptor issue for {pair_id}")
        return None

    # FLANN matcher + ratio test
    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    good_matches = [m for m, n in matches if m.distance < 0.8 * n.distance]

    if len(good_matches) < 10:
        print(f"[!] Only {len(good_matches)} good matches for {pair_id}. Saving debug image.")
        debug_img = cv2.drawMatches(thermal_img, kp1, rgb_img, kp2, good_matches, None,
                                    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        debug_path = os.path.join(OUTPUT_FOLDER, f"{pair_id}_debug_matches.jpg")
        cv2.imwrite(debug_path, debug_img)
        return None

    # Homography
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    if H is None:
        print(f"Homography computation failed — H is None for {pair_id}")
        return None

    # Warp and overlay
    warped = cv2.warpPerspective(thermal_img, H, (rgb_img.shape[1], rgb_img.shape[0]))
    if warped is None or warped.shape[:2] != rgb_img.shape[:2]:
        print(f"Warped image failed or shape mismatch for {pair_id}")
        return None

    gray_aligned = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    normalized = cv2.normalize(gray_aligned, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    thermal_colored = cv2.applyColorMap(normalized, cv2.COLORMAP_JET)
    overlay = cv2.addWeighted(rgb_img, 0.6, thermal_colored, 0.4, 0)

    return overlay

def process_all_images():
    image_files = sorted([f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith('.jpg')])
    paired_ids = set()
    pattern = re.compile(r"^(.*)_(T|Z)\.JPG$", re.IGNORECASE)

    for filename in image_files:
        match = pattern.match(filename)
        if match:
            paired_ids.add(match.group(1))  # Extract XXXX

    for pair_id in paired_ids:
        thermal_path = os.path.join(INPUT_FOLDER, f"{pair_id}_T.JPG")
        rgb_path = os.path.join(INPUT_FOLDER, f"{pair_id}_Z.JPG")

        if not (os.path.exists(thermal_path) and os.path.exists(rgb_path)):
            print(f"Missing pair for {pair_id}, skipping...")
            continue

        thermal_img = cv2.imread(thermal_path)
        rgb_img = cv2.imread(rgb_path)

        if thermal_img is None or rgb_img is None:
            print(f"[!] Could not read one or both images for {pair_id}")
            continue

        overlay_result = align_and_overlay(rgb_img, thermal_img, pair_id)

        if overlay_result is not None:
            out_path = os.path.join(OUTPUT_FOLDER, f"{pair_id}_overlay.jpg")
            cv2.imwrite(out_path, overlay_result)
            print(f"[✓] Saved overlay: {out_path}")
        else:
            print(f"[!] Failed to process {pair_id}")

if __name__ == "__main__":
    process_all_images()
