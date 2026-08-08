import torch
from model_loader import tokenizer, model

LABELS = {
    0: "Hate Speech",
    1: "Offensive Language",
    2: "Neither"
}


def map_label(index, label_name):
    if label_name and isinstance(label_name, str):
        normalized = label_name.lower().replace(" ", "").replace("_", "").replace("-", "")

        if normalized in {"nothate", "not hate", "not-hate", "none", "neutral", "safe", "clean", "normal", "neither"}:
            return "Neither"

        if any(term in normalized for term in ["offens", "abuse", "harass"]):
            return "Offensive Language"

        if any(term in normalized for term in ["hate", "tox"]):
            return "Hate Speech"

    if index in LABELS:
        return LABELS[index]
    return "Neither"


def predict_text(text):
    try:
        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = model(**inputs)

        probabilities = torch.softmax(outputs.logits, dim=1)
        confidence, prediction = torch.max(probabilities, dim=1)

        print("\n==========================")
        print("Input :", text)
        print("Probabilities :", probabilities.tolist())
        print("Prediction Index :", prediction.item())
        print("Model id2label :", model.config.id2label)
        print("==========================\n")

        predicted_index = prediction.item()
        label_name = None
        if hasattr(model, "config") and getattr(model.config, "id2label", None):
            label_name = model.config.id2label.get(predicted_index)
        predicted_label = map_label(predicted_index, label_name)
        return {
            "prediction": predicted_label,
            "confidence": round(confidence.item() * 100, 2)
        }
    except Exception as exc:
        return {
            "prediction": "Unable to classify",
            "confidence": 0.0,
            "error": str(exc)
        }


if model is not None:
    print("Model vocab:", model.config.vocab_size)
    print("Tokenizer vocab:", len(tokenizer))