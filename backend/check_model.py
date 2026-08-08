from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "./saved_model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

print("Model Type:", model.config.model_type)
print("Architecture:", model.config.architectures)
print("Vocab Size:", model.config.vocab_size)
print("Tokenizer Vocab Size:", tokenizer.vocab_size)