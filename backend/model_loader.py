import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification

BASE_DIR = os.path.dirname(__file__)
LOCAL_MODEL_DIR = os.path.join(BASE_DIR, "trained_model")
FALLBACK_MODEL_NAME = "cardiffnlp/twitter-roberta-base-hate-latest"

print("Loading RoBERTa model...")

if os.path.isdir(LOCAL_MODEL_DIR) and os.path.exists(os.path.join(LOCAL_MODEL_DIR, "config.json")):
    print(f"Loading local trained model from {LOCAL_MODEL_DIR}")
    tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(LOCAL_MODEL_DIR)
else:
    print(f"Local model not found, falling back to {FALLBACK_MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(FALLBACK_MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(FALLBACK_MODEL_NAME)

model.eval()

print("RoBERTa model loaded successfully!")