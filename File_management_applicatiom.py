import os
import shutil

def manage_folder(folder):
    file_types = {
        'Images': ['.jpg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.xlsx'],
        'Music': ['.mp3'],
        'Video': ['.mp4'],
        'ZipFiles': ['.zip']
    }

    # Loop through files in the folder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            for directory, extensions in file_types.items():
                if filename.endswith(tuple(extensions)):
                    folder_path = os.path.join(folder, directory)

                    # Create the folder if it doesn't exist
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    # Move the file to the appropriate folder
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved {filename} to {directory}")
                    break  # Stop checking once a match is found

# Provide the correct path
manage_folder(r"E:\A vscode_python_projects\content")