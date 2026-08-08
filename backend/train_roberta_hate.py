import os
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding,
)
from sklearn.metrics import accuracy_score, f1_score
import numpy as np
import torch

MODEL_NAME = "roberta-base"
DATASET_NAME = "cardiffnlp/tweet_eval"
DATASET_CONFIG = "hate"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "trained_model")

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading dataset...")
dataset = load_dataset(DATASET_NAME, DATASET_CONFIG)

print(dataset)

# The target column is usually called 'label' or 'label_text' depending on the dataset.
# TweetEval hate config uses 'label' and 'text'.
if "text" not in dataset["train"].column_names or "label" not in dataset["train"].column_names:
    raise ValueError(f"Unexpected dataset columns: {dataset['train'].column_names}")

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding=True, max_length=128)


print("Tokenizing dataset...")
train_dataset = dataset["train"].select(range(min(1200, len(dataset["train"]))))
val_dataset = dataset["validation"].select(range(min(300, len(dataset["validation"]))))
train_dataset = train_dataset.map(tokenize, batched=True)
val_dataset = val_dataset.map(tokenize, batched=True)

train_dataset = train_dataset.rename_column("label", "labels")
val_dataset = val_dataset.rename_column("label", "labels")

train_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
val_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

print("Loading model...")
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    learning_rate=2e-5,
    num_train_epochs=1,
    weight_decay=0.01,
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_steps=10,
    load_best_model_at_end=False,
    fp16=False,
)


def compute_metrics(pred):
    labels = pred.label_ids
    preds = np.argmax(pred.predictions, axis=1)
    return {
        "accuracy": accuracy_score(labels, preds),
        "f1": f1_score(labels, preds, average="weighted"),
    }


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
    compute_metrics=compute_metrics,
)

print("Starting training...")
trainer.train()

print("Saving model...")
model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print("Training complete. Model saved to", OUTPUT_DIR)
