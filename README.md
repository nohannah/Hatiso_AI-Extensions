# HaTiSo - AI Hate Speech Detection System (Software Course)

## Introduction

HaTiSo is an AI-based hate speech detection system designed to identify and classify harmful comments from social media content.

Before decided choosing RoBERTa model to analyze, there are 3 models have been train which are BERT, RoBERTa and DistilBERT Model. RoBERTa got the best accuacy and perfomace. 
The system uses a transformer-based RoBERTa model to analyze text and classify comments into three categories:

- Hate Speech
- Offensive Language
- Neither

HaTiSo provides real-time prediction through a Flask backend and can be integrated with a Chrome browser extension to analyze comments directly from Facebook.

The system also uses LIME (Local Interpretable Model-Agnostic Explanations) to provide explanations for model predictions, helping users understand why a comment was classified as harmful or non-harmful.

---

## Project Title

**HaTiSo: An AI-Based Hate Speech Detection System Using RoBERTa and Explainable AI**

---

## Main Features

- 🤖 RoBERTa-based text classification
- 🔍 Hate speech detection
- ⚠️ Offensive language detection
- ✅ Non-harmful comment detection
- 📊 Prediction confidence score
- 💡 Explainable AI using LIME
- 🌐 Flask REST API
- 🗄️ SQLite prediction history
- 🌐 Chrome browser extension
- 📱 Facebook comment analysis
- ⚡ Real-time prediction

---

# System Architecture

The system follows this workflow:

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
Result displayed in Facebook

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
│   ├── app.py
│   └── ...
│
├── dashboard/
│   └── ...
│
├── extension/
│   ├── manifest.json
│   ├── content.js
│   ├── ...
│   └── ...
│
├── .gitignore
├── README.md
└── requirements.txt
