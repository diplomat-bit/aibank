from transformers import BertTokenizer, BertForSequenceClassification
import torch

MODEL_PATH = '/content/drive/MyDrive/output'
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

def predict(input_text):
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        result = probabilities[0].tolist() # Assuming binary classification; adjust as needed
        return {"positive": result[1], "negative": result[0]}
