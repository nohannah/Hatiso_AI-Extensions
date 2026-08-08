# HaTiSo AI Extensions - Setup Guide

This guide explains how to download, install, configure, and run the HaTiSo AI Extensions project.

---

## 1. Introduction

HaTiSo AI Extensions is an AI-based hate speech detection system designed to analyze social media comments using a transformer-based language model.

The system combines:

- RoBERTa for text classification
- Flask for the backend API
- LIME for Explainable AI
- SQLite for prediction history
- JavaScript, HTML, and CSS for the interface
- Chrome Extension for browser-based Facebook comment analysis

The system can classify comments into three categories:

- **Hate Speech**
- **Offensive Language**
- **Neither**

---

# 2. System Workflow

The basic workflow is:

```text
Facebook Comment
       ↓
Chrome Extension
       ↓
Flask API
       ↓
RoBERTa Model
       ↓
Prediction
       ↓
LIME Explanation
       ↓
Result
```

---

# 3. Requirements

Before installing HaTiSo, make sure the computer has:

- Python 3.10 or newer
- Git
- Google Chrome
- Internet connection

---

# 4. Download the Project

Open Command Prompt (CMD).

Clone the repository:

```cmd
git clone https://github.com/nohannah/Hatiso_AI-Extensions.git
```

Enter the project folder:

```cmd
cd Hatiso_AI-Extensions
```

---

# 5. Create a Python Virtual Environment

Create a virtual environment:

```cmd
python -m venv backend\venv
```

This creates a local Python environment inside:

```text
backend/
└── venv/
```

The `venv` folder is intentionally not included in GitHub.

Each user should create their own virtual environment.

---

# 6. Activate the Virtual Environment

On Windows:

```cmd
backend\venv\Scripts\activate
```

After activation, CMD should show something similar to:

```text
(venv) C:\...\Hatiso_AI-Extensions>
```

---

# 7. Install Dependencies

After activating the virtual environment, install the required Python packages:

```cmd
pip install -r requirements.txt
```

If `pip` does not work, use:

```cmd
python -m pip install -r requirements.txt
```

---

# 8. Model Setup

The trained RoBERTa model is not included directly in the GitHub repository because transformer model files can be very large.

The required model must be placed in the model directory expected by the backend.

Example:

```text
backend/
└── saved_model/
    ├── config.json
    ├── tokenizer.json
    ├── tokenizer_config.json
    └── model files
```

Make sure the model path used by the backend matches the location of the downloaded model.

> **Important:** The application cannot perform predictions without the required trained model.

---

# 9. Start the Flask Backend

From the project root, activate the virtual environment:

```cmd
backend\venv\Scripts\activate
```

Start the Flask application:

```cmd
python backend\app.py
```

The backend should run at:

```text
http://127.0.0.1:5000
```

Keep this CMD window open while using the Chrome extension.

---

# 10. Test the Backend

Open Google Chrome and visit:

```text
http://127.0.0.1:5000
```

If the backend is running correctly, the HaTiSo web interface should load.

---

# 11. Install the Chrome Extension

Open Google Chrome.

Go to:

```text
chrome://extensions/
```

### Step 1

Turn on:

**Developer mode**

### Step 2

Click:

**Load unpacked**

### Step 3

Select the project's:

```text
extension
```

folder.

For example:

```text
Hatiso_AI-Extensions/
└── extension/
```

The HaTiSo extension should now appear in Chrome.

---

# 12. Use HaTiSo on Facebook

Make sure the Flask backend is running.

Then:

1. Open Facebook.
2. Open a page containing comments.
3. Find a comment.
4. The Chrome extension detects the comment.
5. The comment is sent to the Flask API.
6. RoBERTa analyzes the comment.
7. The prediction is returned.
8. The result is displayed to the user.

---

# 13. Prediction Categories

HaTiSo provides three classification categories.

## Hate Speech

The comment contains hateful or discriminatory content.

## Offensive Language

The comment contains insulting, abusive, or offensive language but may not necessarily constitute hate speech.

## Neither

The comment does not contain hate speech or offensive language.

---

# 14. Explainable AI with LIME

HaTiSo uses LIME (Local Interpretable Model-Agnostic Explanations) to help explain individual predictions.

LIME identifies words or parts of the input that contribute to the model's prediction.

This allows users to understand not only the prediction but also some of the reasons behind it.

---

# 15. Prediction History

HaTiSo uses SQLite to store prediction history.

The system can store information such as:

- Comment
- Prediction
- Confidence
- Timestamp

The database is generated locally and is not stored in GitHub.

---

# 16. Project Structure

```text
Hatiso_AI-Extensions/
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

# 17. Troubleshooting

## Python is not recognized

Check Python:

```cmd
python --version
```

If Python is not recognized, install Python and make sure it is added to the Windows PATH.

---

## pip is not recognized

Try:

```cmd
python -m pip --version
```

Then:

```cmd
python -m pip install -r requirements.txt
```

---

## ModuleNotFoundError

Make sure the virtual environment is activated:

```cmd
backend\venv\Scripts\activate
```

Then:

```cmd
pip install -r requirements.txt
```

---

## Flask does not start

Make sure you are in the project root:

```text
Hatiso_AI-Extensions
```

Then run:

```cmd
python backend\app.py
```

---

## Chrome extension cannot be loaded

Open:

```text
chrome://extensions/
```

Check that:

- Developer mode is enabled.
- You selected the `extension` folder.
- `manifest.json` exists inside the extension folder.

---

## Prediction does not work

Check that:

1. Flask is running.
2. The trained RoBERTa model is available.
3. The model path is correct.
4. The Chrome extension is enabled.
5. The backend is accessible at:

```text
http://127.0.0.1:5000
```

---

# 18. Stopping HaTiSo

To stop Flask:

```text
CTRL + C
```

To deactivate the virtual environment:

```cmd
deactivate
```

---

# 19. Development Guide

Before making changes, get the latest version:

```cmd
git pull origin main
```

Check your changes:

```cmd
git status
```

Add your changes:

```cmd
git add .
```

Create a commit:

```cmd
git commit -m "Describe your changes"
```

Push to GitHub:

```cmd
git push
```

---

# 20. Important Files Not Stored in GitHub

The following are intentionally excluded:

```text
venv/
.venv/
__pycache__/
*.pyc
.env
*.db
*.sqlite
backend/trained_model/
backend/saved_model/
```

These files are either generated locally, contain private information, or may be too large for a normal GitHub repository.

---

# 21. Quick Start

For experienced users:

```cmd
git clone https://github.com/nohannah/Hatiso_AI-Extensions.git

cd Hatiso_AI-Extensions

python -m venv backend\venv

backend\venv\Scripts\activate

pip install -r requirements.txt

python backend\app.py
```

Then open:

```text
http://127.0.0.1:5000
```

and load the `extension` folder through:

```text
chrome://extensions/
```

---

# HaTiSo AI Extensions

**AI-Based Hate Speech Detection Using RoBERTa and Explainable AI**

Developed for educational and research purposes.
