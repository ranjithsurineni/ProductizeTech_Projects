# AI Engineering Assignment – Task Series

This repository contains three AI-based tasks executed as part of an assignment. Each task demonstrates a different image processing or automation pipeline using Python and relevant libraries.

---

## ✅ Task 1 – RGB-Thermal Image Overlay Algorithm

### 🎯 Objective:
To overlay thermal and RGB images based on filename patterns, ensuring correct alignment and visualization of detected objects.

### 📌 Key Features:
- Automatically categorizes input images using filename suffixes (`_T.JPG` for thermal, `_Z.JPG` for RGB).
- Aligns and overlays RGB and thermal images for visual analysis.
- Displays side-by-side and overlaid results for comparison.

### 🛠️ Tools & Libraries:
- `OpenCV`
- `NumPy`
- `Matplotlib`
- `os`

---

## ✅ Task 2 – Change Detection Algorithm

### 🎯 Objective:
To detect and highlight changes between "before" and "after" images of the same scene.

### 📌 Key Features:
- Image differencing using absolute subtraction.
- Thresholding to extract meaningful differences.
- Morphological operations for noise removal.
- Bounding box generation on changed regions.
- Output image with highlighted changes.

### 🛠️ Techniques Used:
- Grayscale conversion
- Gaussian blur
- Absolute difference
- Thresholding (`cv2.threshold`)
- Dilation for enhancement

### 🛠️ Tools & Libraries:
- `OpenCV`
- `NumPy`
- `os`
- `argparse`

---

## ✅ Task 3 – GLR Pipeline with Streamlit

### 🎯 Objective:
To build an automated **Generalized Letter Renderer (GLR)** pipeline using **Streamlit**, supporting:
- Key-Value pair extraction
- Document template population
- Downloadable final document output

### 📌 Key Features:
- Interactive UI using Streamlit
- Upload JSON key-value file
- Auto-fills predefined Word (.docx) template with values
- Generates and downloads final letter

### 🛠️ Tools & Libraries:
- `Streamlit`
- `python-docx`
- `json`
- `io`
- `base64`

---

## 🧰 Setup Instructions

1. **Clone the Repository:**
   ```bash
    https://github.com/ranjithsurineni/ProductizeTech_Projects.git
    cd ProductizeTech_Projects
   ```
2. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. Run Streamlit App (for Task 3):
   ```bash
   streamlit run Task-*.py
   ```

---
### 📬 Contact

Ranjith Kumar Surineni

[Email Me](mailto:ranjithsurineni.official@gmail.com)

[LinkedIn](https://www.linkedin.com/in/ranjith-kumar-surineni-b73b981b6/)
