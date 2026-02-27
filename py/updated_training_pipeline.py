
# Import required libraries
import json
import torch
import time
import zipfile
import xml.etree.ElementTree as ET
from torch.utils.data import DataLoader, TensorDataset, ConcatDataset
from transformers import BertForSequenceClassification, BertTokenizer, AdamW
from sklearn.metrics import precision_score, recall_score, f1_score, r2_score
from datasets import load_dataset
from concurrent.futures import ThreadPoolExecutor

# Initialize the clock for time estimation
start_time = time.time()

# Load custom Hugging Face dataset
print("Loading Hugging Face dataset...")
hugging_face_dataset = load_dataset("Admin08077/Taxonomy")  # Replace with your dataset

# Load the fine-tuned BERT model
print("Loading the fine-tuned BERT model...")
finetuned_bert_model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
finetuned_bert_model.load_state_dict(torch.load('/content/drive/MyDrive/000/Model.pt'))

# Load new training data from XML
print("Loading new training data from XML...")
tree = ET.parse('/content/drive/MyDrive/000/FeatureExtractor.xml')
root = tree.getroot()
text_data = [elem.text for elem in root.findall('.//Text')]

# Tokenize XML data
print("Tokenizing XML data...")
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer(text_data, padding=True, truncation=True, return_tensors='pt')
input_ids = tokens['input_ids']
attention_mask = tokens['attention_mask']

# Dummy labels (replace with your actual labels)
labels = torch.tensor([0] * len(text_data))

# Create DataLoader for XML data
print("Creating DataLoader for XML data...")
xml_dataset = TensorDataset(input_ids, attention_mask, labels)
xml_dataloader = DataLoader(xml_dataset, batch_size=32)

# Combine both datasets
print("Combining both datasets...")
combined_dataset = ConcatDataset([hugging_face_dataset, xml_dataset])
combined_dataloader = DataLoader(combined_dataset, batch_size=32)

# Initialize and train the model
print("Starting training...")
optimizer = AdamW(finetuned_bert_model.parameters(), lr=1e-5)

def train_batch(batch):
    batch_input_ids, batch_attention_mask, batch_labels = batch
    optimizer.zero_grad()
    outputs = finetuned_bert_model(input_ids=batch_input_ids, attention_mask=batch_attention_mask, labels=batch_labels)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    return loss.item()

# Parallelizing the training
with ThreadPoolExecutor() as executor:
    for i, batch in enumerate(combined_dataloader):
        batch_start_time = time.time()
        loss = executor.submit(train_batch, batch)
        batch_time = time.time() - batch_start_time
        remaining_time = batch_time * (len(combined_dataloader) - i - 1)
        print(f"Batch {i+1}/{len(combined_dataloader)} completed. Loss: {loss.result()}. Estimated time remaining: {remaining_time:.2f}s")

# Save the retrained model and other necessary files
print("Saving files...")
torch.save(finetuned_bert_model.state_dict(), '/content/drive/MyDrive/000/retrained_model.pt')
tokenizer.save_pretrained('/content/drive/MyDrive/000/tokenizer')
with open('/content/drive/MyDrive/000/config.json', 'w') as f:
    json.dump(finetuned_bert_model.config.to_dict(), f)

# Zip the saved files
print("Zipping files...")
with zipfile.ZipFile('/content/drive/MyDrive/000/retrained_model_files.zip', 'w') as zipf:
    zipf.write('/content/drive/MyDrive/000/retrained_model.pt', 'retrained_model.pt')
    zipf.write('/content/drive/MyDrive/000/tokenizer', 'tokenizer')
    zipf.write('/content/drive/MyDrive/000/config.json', 'config.json')

print(f"Training completed. Total time elapsed: {time.time() - start_time:.2f}s")
print(f"All files zipped and saved at /content/drive/MyDrive/000/retrained_model_files.zip")
