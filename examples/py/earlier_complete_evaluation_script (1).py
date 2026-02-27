import json

import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from torch.utils.data import ConcatDataset, DataLoader, TensorDataset

# Path to the saved model and config files
MODEL_PATH = "/content/drive/MyDrive/000/extracted_model_files/retrained_model.pt"
CONFIG_PATH = "/content/drive/MyDrive/000/extracted_model_files/config.json"

# Load the model and config
with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

model = nn.DataParallel(torch.load(MODEL_PATH))
model.eval()

# Assuming your validation data is loaded into val_loader

# Validation loop
all_labels = []
all_predictions = []

with torch.no_grad():
    for inputs, labels in val_loader:
        outputs = model(inputs)
        predictions = torch.argmax(outputs, dim=1)

        all_labels.extend(labels.cpu().numpy())
        all_predictions.extend(predictions.cpu().numpy())

# Calculate metric scores
accuracy = accuracy_score(all_labels, all_predictions)
precision = precision_score(all_labels, all_predictions, average="weighted")
recall = recall_score(all_labels, all_predictions, average="weighted")
f1 = f1_score(all_labels, all_predictions, average="weighted")

# Print metric scores
print("Validation Metrics:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Assuming xml_input_ids, xml_attention_mask, xml_labels are defined
# Create XML dataset and dataloader
batch_size = 32


def create_xml_dataset(xml_input_ids, xml_attention_mask, xml_labels, batch_size):
    xml_dataset = TensorDataset(xml_input_ids, xml_attention_mask, xml_labels)
    xml_dataloader = DataLoader(xml_dataset, batch_size=batch_size, shuffle=True)
    return xml_dataloader


xml_dataloader = create_xml_dataset(
    xml_input_ids, xml_attention_mask, xml_labels, batch_size
)

# Combine XML DataLoader and the validation DataLoader
combined_dataloader = DataLoader(
    ConcatDataset([xml_dataloader.dataset, val_loader.dataset]),
    batch_size=batch_size,
    shuffle=True,
)
