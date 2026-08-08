from lime.lime_text import LimeTextExplainer
import numpy as np
import torch

from model_loader import tokenizer, model

# The class names shown in the explanation
CLASS_NAMES = [
    "Hate Speech",
    "Offensive Language",
    "Neither"
]

# Create the LIME explainer
explainer = LimeTextExplainer(
    class_names=CLASS_NAMES
)


def predict_proba(texts):
    """
    LIME requires a function that returns prediction
    probabilities for multiple texts.
    """

    probabilities = []

    for text in texts:

        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = model(**inputs)

        probs = torch.softmax(
            outputs.logits,
            dim=1
        )

        probabilities.append(
            probs.numpy()[0]
        )

    return np.array(probabilities)


def explain_prediction(text):

    explanation = explainer.explain_instance(
        text,
        predict_proba,
        num_features=5,
        num_samples=100
    )

    results = []

    for word, weight in explanation.as_list():

        results.append({

            "word": word,

            "weight": round(weight, 3)

        })

    return results