# Google Colaboratory Script to Extract and Zip Files
import glob
import os
import zipfile

# Define the new and old paths
old_base_path = "/content/drive/MyDrive/sdk/Australia-ConsumerDataStandards_Digital_Regulatory.yaml_4/aspnetcore/src/IO.Swagger/Models/"
new_base_path = "/new/path/to/files/"  # Update this to the new path

# Initialize a ZipFile
with zipfile.ZipFile("extracted_files.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
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

# The Zip file "extracted_files.zip" will contain all the files found in the new path.
