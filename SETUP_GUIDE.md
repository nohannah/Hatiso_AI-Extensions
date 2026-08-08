# HaTiSo Setup Guide

This guide explains how to download, install, configure, and run the HaTiSo AI Hate Speech Detection System.

---

## 1. Requirements

Before starting, install:

- Python 3.10 or newer
- Git
- Google Chrome
- Internet connection

---

## 2. Download the Project

Open Command Prompt (CMD) and run:

```cmd
git clone https://github.com/nohannah/HateSpeechDetector.git
```

Enter the project folder:

```cmd
cd HateSpeechDetector
```

---

## 3. Create a Python Virtual Environment

Create a virtual environment inside the backend folder:

```cmd
python -m venv backend\venv
```

This creates:

```text
backend/
└── venv/
```

The `venv` folder is not included in GitHub because each user should create their own environment.

---

## 4. Activate the Virtual Environment

On Windows, run:

```cmd
backend\venv\Scripts\activate
```

After activation, you should see:

```text
(venv) C:\...\HateSpeechDetector>
```

---

## 5. Install Required Packages

Make sure the virtual environment is activated.

Then run:

```cmd
pip install -r requirements.txt
```

This installs the Python libraries required by HaTiSo.

---

## 6. Model Setup

The trained RoBERTa model is not included directly in this GitHub repository because trained transformer models can be very large.

Before running the application, place the required model files in the model directory specified by the project.

Example:

```text
backend/
└── saved_model/
    ├── config.json
    ├── tokenizer_config.json
    ├── tokenizer.json
    └── model files
```

Make sure the model path used by the Python code matches the location of the model.

---

## 7. Start the Flask Backend

From the main project folder, activate the environment:

```cmd
backend\venv\Scripts\activate
```

Then start the Flask server:

```cmd
python backend\app.py
```

If successful, the backend should run at:

```text
http://127.0.0.1:5000
```

Keep the CMD window open while using HaTiSo.

---

## 8. Test the Backend

Open Google Chrome and visit:

```text
http://127.0.0.1:5000
```

The HaTiSo web application should appear.

---

## 9. Install the Chrome Extension

Open Google Chrome.

Go to:

```text
chrome://extensions/
```

### Step 1

Enable:

**Developer mode**

### Step 2

Click:

**Load unpacked**

### Step 3

Select:

```text
HateSpeechDetector/extension
```

The HaTiSo extension should now appear in your installed extensions.

---

## 10. Use HaTiSo on Facebook

Make sure the Flask backend is running.

Then:

1. Open Facebook.
2. Open a page containing comments.
3. Find a comment.
4. The HaTiSo Chrome extension analyzes the comment.
5. The comment is sent to the Flask API.
6. The RoBERTa model predicts the category.
7. The result is returned to the extension.
8. The prediction and confidence are displayed.

---

## 11. Prediction Categories

HaTiSo classifies comments into three categories:

### Hate Speech

Content containing hateful or discriminatory language.

### Offensive Language

Insulting, abusive, or offensive language that may not necessarily constitute hate speech.

### Neither

Comments that do not contain hate speech or offensive language.

---

## 12. Explainable AI

HaTiSo uses LIME to help explain model predictions.

LIME identifies words or parts of the input that contributed to the prediction.

The system can therefore provide not only a prediction but also an explanation of the prediction.

---

## 13. Troubleshooting

### Problem: `python` is not recognized

Install Python and make sure Python is added to the Windows PATH.

Check Python:

```cmd
python --version
```

---

### Problem: `pip` is not recognized

Try:

```cmd
python -m pip --version
```

Then install packages using:

```cmd
python -m pip install -r requirements.txt
```

---

### Problem: `ModuleNotFoundError`

Make sure the virtual environment is activated:

```cmd
backend\venv\Scripts\activate
```

Then install the dependencies:

```cmd
pip install -r requirements.txt
```

---

### Problem: Flask does not start

Make sure you are in the project root:

```text
HateSpeechDetector
```

Then run:

```cmd
python backend\app.py
```

---

### Problem: Chrome extension cannot be loaded

Go to:

```text
chrome://extensions/
```

Make sure:

- Developer mode is enabled.
- You selected the `extension` folder.
- `manifest.json` exists inside the extension folder.

---

### Problem: Prediction does not work

Check that:

1. The Flask backend is running.
2. The model files are available.
3. The model path is correct.
4. The Chrome extension is loaded.
5. The browser can connect to:

```text
http://127.0.0.1:5000
```

---

## 14. Stopping the Application

To stop the Flask server, go to the CMD window running Flask and press:

```text
CTRL + C
```

To deactivate the virtual environment:

```cmd
deactivate
```

---

# Project Structure

```text
HateSpeechDetector/
│
├── backend/
│   ├── database/
│   ├── model/
│   ├── static/
│   ├── templates/
│   ├── utils/
│   └── app.py
│
├── dashboard/
│
├── extension/
│   ├── manifest.json
│   ├── content.js
│   └── ...
│
├── .gitignore
├── README.md
├── SETUP_GUIDE.md
└── requirements.txt
```

---

# Development

If you make changes to the project:

```cmd
git status
```

Add your changes:

```cmd
git add .
```

Commit:

```cmd
git commit -m "Describe your changes"
```

Push to GitHub:

```cmd
git push
```

---

# Important Note

The following files are intentionally not stored in GitHub:

```text
venv/
__pycache__/
*.pyc
.env
*.db
*.sqlite
backend/trained_model/
backend/saved_model/
```

These files are either generated automatically, contain local information, or may be too large for a normal GitHub repository.

---

# HaTiSo

**AI-Based Hate Speech Detection System**

Developed for educational and research purposes.
