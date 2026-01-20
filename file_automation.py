# CodeAlpha Task 3 - File Automation Script
# This script moves all .jpg files from source folder to destination folder

import os
import shutil

# Define source and destination folders
source_folder = "source_file"
destination_folder = "destination_file"

# Check if folders exist
if not os.path.exists(source_folder):
    print("❌ Source folder does not exist.")
elif not os.path.exists(destination_folder):
    print("❌ Destination folder does not exist.")
else:
    files_moved = 0

    # Loop through files in source folder
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)

            shutil.move(source_path, destination_path)
            files_moved += 1
            print(f"✅ Moved: {file_name}")

    if files_moved == 0:
        print("ℹ️ No .jpg files found to move.")
    else:
        print(f"\n🎉 Total .jpg files moved: {files_moved}")

