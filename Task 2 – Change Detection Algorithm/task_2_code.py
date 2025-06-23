import cv2
import numpy as np
import os

def change_detection(input_folder, output_folder, min_contour_area=500):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files ending with .jpg that do not contain ~2
    before_images = [f for f in os.listdir(input_folder) if f.endswith('.jpg') and '~2' not in f]

    for before_filename in before_images:
        # Derive after filename from before filename
        after_filename = before_filename.replace('.jpg', '~2.jpg')

        before_path = os.path.join(input_folder, before_filename)
        after_path = os.path.join(input_folder, after_filename)

        # Check if after image exists
        if not os.path.exists(after_path):
            print(f"After image for {before_filename} not found, skipping.")
            continue

        # Load images
        before_img = cv2.imread(before_path)
        after_img = cv2.imread(after_path)

        if before_img is None or after_img is None:
            print(f"Error loading images {before_filename} or {after_filename}")
            continue

        # Convert to grayscale for comparison
        before_gray = cv2.cvtColor(before_img, cv2.COLOR_BGR2GRAY)
        after_gray = cv2.cvtColor(after_img, cv2.COLOR_BGR2GRAY)

        # Compute absolute difference
        diff = cv2.absdiff(before_gray, after_gray)

        # Threshold to get binary image of changes
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        # Morphological operations to remove noise and fill gaps
        kernel = np.ones((5,5), np.uint8)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # Find contours of changed regions
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding boxes around significant contours (missing objects)
        output_img = after_img.copy()
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > min_contour_area:
                # Draw bounding box or polygon (bounding box here)
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(output_img, (x,y), (x+w, y+h), (0,0,255), 2)  # Red box

        # Save output image with highlights
        output_filename = before_filename.replace('.jpg', '~2_highlighted.jpg')
        output_path = os.path.join(output_folder, output_filename)
        cv2.imwrite(output_path, output_img)
        print(f"Processed {before_filename} and saved output to {output_filename}")

if __name__ == "__main__":
    input_folder = "input-images"
    output_folder = "output-images"
    change_detection(input_folder, output_folder)
