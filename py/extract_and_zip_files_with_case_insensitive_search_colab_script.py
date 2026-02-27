# Google Colaboratory Script to Extract, Zip Files, and Find "Models" Folders
import glob
import os
import zipfile

from google.colab import drive

# Mount Google Drive
drive.mount("/content/drive")


def find_model_folders(base_path):
    # Find all folders named "Models", "Model", "models", or "model" and not empty
    model_folders = []
    for root, dirs, files in os.walk(base_path):
        if os.path.basename(root).lower() in ["models", "model"] and (dirs or files):
            model_folders.append(root)
    return model_folders


# Define the new and old paths
old_base_path = "/content/drive/MyDrive/sdk/Australia-ConsumerDataStandards_Digital_Regulatory.yaml_4/aspnetcore/src/IO.Swagger/Models/"
new_base_path = "/content/drive/MyDrive/000/"  # Updated new_base_path
google_drive_save_path = "/content/drive/MyDrive/000/"

# Initialize a ZipFile
zip_file_path = os.path.join(google_drive_save_path, "extracted_files.zip")
with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    # Loop through all the file names extracted from the log
    for (
        file_name
    ) in (
        extracted_file_names
    ):  # Assume this variable holds the list of file names without paths
        # Construct the old and new full paths
        old_full_path = os.path.join(old_base_path, file_name)
        new_full_path = os.path.join(new_base_path, file_name)

        # Search for the file in the new location
        search_results = glob.glob(f"{new_base_path}/**/{file_name}", recursive=True)

        # If the file is found, add it to the ZipFile
        if search_results:
            actual_new_path = search_results[0]
            zipf.write(actual_new_path, os.path.basename(actual_new_path))
        else:
            print(f"File {file_name} not found in the new path.")

# Find all non-empty "Models" or "Model" folders (case-insensitive)
model_folders = find_model_folders(new_base_path)
print("Non-empty 'Models' or 'Model' folders:")
for folder in model_folders:
    print(folder)
