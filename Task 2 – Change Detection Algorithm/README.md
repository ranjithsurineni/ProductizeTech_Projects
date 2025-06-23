# Change Detection Algorithm - Detailed Report

## Overview

This project implements a **Change Detection** algorithm that detects and highlights differences between pairs of aligned images representing the same scene taken before and after a change. The goal is to automatically identify objects or regions that have disappeared or changed in the "after" image compared to the "before" image.

---

## Objective

- Detect and localize changes between “before” and “after” images.
- Highlight these changes visually by drawing bounding boxes around missing or altered objects in the after images.
- Automate this process for multiple image pairs in a folder, generating annotated output images for review.

---

## Input and Output Specifications

- **Input**: A folder containing paired images named according to the following convention:
  - Before image: `X.jpg`
  - After image: `X~2.jpg`
- **Output**: Annotated after images with detected changes highlighted by bounding boxes, saved in a specified output folder.

---

## Algorithm and Techniques Used

### 1. Image Preprocessing

- **Grayscale Conversion**:  
  Both input images are converted from color (BGR) to grayscale to simplify the data, reducing computational complexity while preserving structural information relevant for detecting changes.

### 2. Image Differencing

- **Absolute Difference Calculation**:  
  We calculate the absolute pixel-wise difference between the before and after grayscale images. This highlights the regions where pixel intensity has changed, revealing areas of change in the scene.

### 3. Thresholding

- **Binary Thresholding**:  
  A threshold is applied to the difference image to convert it into a binary mask. Pixels with intensity difference above a set threshold (e.g., 30) are considered changed, while those below are considered unchanged. This step filters out minor variations due to noise or illumination changes.

### 4. Morphological Operations

- **Noise Removal and Gap Filling**:  
  Morphological operations, specifically closing followed by opening with a kernel, are applied to the binary mask to:
  - Close small holes or gaps within detected regions (closing).
  - Remove small isolated noise pixels (opening).  
  These operations refine the mask to produce more coherent, cleaner regions representing actual changes.

### 5. Contour Detection

- **Finding Changed Regions**:  
  Contours (continuous boundaries of connected components) are extracted from the refined binary mask. Each contour corresponds to a candidate region where a change has occurred.

### 6. Filtering Contours by Area

- **Noise Reduction by Area Thresholding**:  
  Small contours below a minimum area threshold (e.g., 500 pixels) are discarded to avoid false positives caused by noise or insignificant changes.

### 7. Highlighting Changes

- **Bounding Boxes Drawing**:  
  For each significant contour, a bounding rectangle is drawn on the after image in red color. This visually highlights the location and extent of missing or changed objects.

---

## Technical Details and Libraries Used

- **Python 3.x**
- **OpenCV** (`cv2`): Used for image loading, processing, difference calculation, thresholding, morphological transformations, contour detection, and drawing annotations.
- **NumPy**: For numerical operations, specifically creating morphological kernels.

---

## Assumptions and Limitations

- The input image pairs are **100% aligned** and of the same resolution, simplifying pixel-wise comparison.
- Illumination conditions are assumed similar; significant lighting changes may lead to false detections.
- The method detects any pixel-level change, so minor differences due to shadows or reflections may occasionally be highlighted.
- Bounding boxes are used for simplicity; polygons could provide more precise outlines but are more complex to implement.

---

## Folder Structure Example

/input_folder
    ├── 1.jpg
    ├── 1~2.jpg
    ├── 2.jpg
    ├── 2~2.jpg
    └── ...
/task_2_output
    ├── 1.jpg
    ├── 1~2_highlighted.jpg
    ├── 2.jpg
    ├── 2~2_highlighted.jpg
    └── ...
└── task_2_code.py
├──requirement.txt
└── README.md


---

## Conclusion

This project implements a robust, efficient pipeline for detecting and highlighting changes between paired images using classical computer vision techniques. The solution provides actionable visual output for monitoring scene changes, useful for surveillance, inspection, or remote sensing applications. The modular and extensible design allows easy integration and future improvements leveraging more advanced algorithms.

---