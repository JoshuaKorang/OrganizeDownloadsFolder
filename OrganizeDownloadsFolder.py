import os
import shutil
from pathlib import Path

# Define the file categories and corresponding file extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.m4a'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Installers': ['.exe', '.msi', '.dmg'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.ipynb'],
}

# Define the source folder (Downloads folder)
DOWNLOADS_FOLDER = str(Path.home() / "Downloads")

def organize_downloads():
    # Create subfolders for each file category if they don't exist
    for folder_name in FILE_CATEGORIES.keys():
        folder_path = os.path.join(DOWNLOADS_FOLDER, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Loop through all the files in the Downloads folder
    for file_name in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        _, file_extension = os.path.splitext(file_name)
        
        # Find the correct category for the file
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                dest_folder = os.path.join(DOWNLOADS_FOLDER, category)
                shutil.move(file_path, os.path.join(dest_folder, file_name))
                print(f"Moved: {file_name} to {category}")
                moved = True
                break
        
        # If the file type is unknown, move it to a 'Miscellaneous' folder
        if not moved:
            misc_folder = os.path.join(DOWNLOADS_FOLDER, "Miscellaneous")
            if not os.path.exists(misc_folder):
                os.makedirs(misc_folder)
            shutil.move(file_path, os.path.join(misc_folder, file_name))
            print(f"Moved: {file_name} to Miscellaneous")

if __name__ == "__main__":
    organize_downloads()
