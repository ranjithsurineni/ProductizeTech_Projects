# 📄 Task 3 – GLR Pipeline

## ✅ Project Overview

This assignment delivers a powerful, intelligent report automation system that uses **LLM-based NLP** to extract data from unstructured inspection PDF files and auto-fills an insurance `.docx` template with contextually relevant information.

The system is developed using:
- 🧠 **mistralai/mistral-small-3.2-24b** via **OpenRouter API**
- 🧾 **Python + Streamlit** frontend
- 📄 **.docx Template Parsing**
- 📑 **PDF Inspection Report Reading**
- 📥 Auto-generated editable final document for download

---

## 🛠️ Tools & Technologies Used

| Component      | Tool/Library                                      |
|----------------|---------------------------------------------------|
| Frontend       | `Streamlit` (for local web interface)             |
| PDF Processing | `PyMuPDF` (`fitz`) for text extraction            |
| Template Parsing | `python-docx` for .docx placeholders            |
| LLM API        | `OpenRouter` + `mistralai/mistral-small-3.2-24b`                        |
| NLP Task       | Prompt-based extraction via LLM                   |
| Data Parsing   | `regex`, `json`, `requests`                       |
| Output         | Streamed download of filled `.docx` document      |

---

## ⚙️ Algorithms & Techniques Used

### 🔍 Text Extraction
- PDF files are parsed page-by-page using **PyMuPDF (fitz)**.
- All extracted raw text is passed as context to the LLM.

### 📌 Placeholder Identification
- The `.docx` template is scanned using regex to find placeholders in the format:  



### 🧠 LLM-Based Key-Value Extraction
- A structured prompt is sent to **mistralai/mistral-small-3.2-24b via OpenRouter** to:
- Identify values for each `[FIELD]`
- Return a **clean JSON object** mapping field → value

### 📄 Template Auto-Fill
- Using `python-docx`, each placeholder in the `.docx` is replaced with the value from the LLM’s JSON output.

---

## 🔁 Workflow / Functionality

1. 📤 **Upload** the following:
 - `.docx` Template with `[FIELD]` placeholders
 - One or more `.pdf` files containing inspection text

2. 🧠 **Text Extraction**:
 - PDF text is extracted and compiled into a single input.

3. 🤖 **LLM API Call**:
 - Prompt is sent to mistralai/mistral-small-3.2-24b via OpenRouter
 - Returns a JSON of field-value mappings

4. 📄 **Docx Generation**:
 - The original template is updated with values
 - Final `.docx` file is streamed for user download

5. ✅ Final report is downloadable, viewable, and editable.

---

## 📦 Project File Structure

📁 Task 3 - GLR Pipeline/
    ├── app.py # Main Streamlit app
    ├── requirements.txt # Required Python packages
    ├── Example 1 - USAA # Template with placeholders (example)
    ├── Example 2 - Wayne-Elevate
    ├── Example 3 - Guide One - Eberl
    ├── /pdf_reports # Uploaded PDF files
    |    └── 📥 Output: filled_report.docx 
    └── requirements.txt

---

## 🧪 Sample Placeholders in Template

```bash

[DATE_LOSS]
[INSURED_NAME]
[INSURED_H_STREET]
[INSURED_H_CITY]
[INSURED_H_STATE]
[INSURED_H_ZIP]
[MORTGAGEE]
[TOL_CODE]
[DATE_RECEIVED]

```


These placeholders are dynamically filled by the model based on the PDF contents.

---

## 🚀 How to Run the Project

### 1. 🔧 Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Run Locally
```bash
streamlit run app.py
```

### 3. Use the Web Interface

Upload .docx template and one or more .pdf reports

Click “🔄 Generate Report”

Download the filled .docx report

---

# Sample Prompt Logic (sent to mistralai/mistral-small-3.2-24b)

You are an AI assistant helping fill an insurance report.

Below are placeholders that need to be filled in:
[DATE_LOSS], [INSURED_NAME], ...

Based on the following inspection report, extract values for the above fields and return only a JSON object...

Inspection Report:
(PDF Extracted Text Here)

---

### Error Handling

| Error Type                      | Handling Strategy                                |
| ------------------------------- | ------------------------------------------------ |
| ❌ API Timeout or 403            | User-friendly message + raw response shown       |
| ❌ JSON Parsing Error            | Regex fallback + debug message shown             |
| ❌ Invalid template placeholders | Missing values are skipped gracefully            |
| ❌ No extracted fields           | App prompts for re-upload or template correction |

---

### Limitations

The template must use [FIELD_NAME] format.

Extracted text quality highly affects the model's performance.

Complex or nested fields may need manual edits post-download.

---

## Author

Ranjith Kumar Surineni
Data Scientist & AI Engineer
📧 ranjithsurineni.official@gmail.com
🔗 LinkedIn
🧠 Passionate about automating complex workflows with AI