import os
import shutil

source_folder = r'C:\Users\Hamza Computer\Desktop\test_folder'

folder = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    "Documents": ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "Audio": ['.mp3', '.wav', '.aac', '.flac'],
    "Videos": ['.mp4', '.avi', '.mov', '.mkv']
}
#to list all files in the folder (os.listdir)
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
        
    if os.path.isdir(file_path):
        continue
    
#os.path.splitext → file ka extension nikalta hai
    _, ext = os.path.splitext(file)

    # Move file into correct folder
    for folder_name, extensions in folder.items():
        if ext.lower() in extensions:
            folder_path = os.path.join(source_folder, folder_name)

            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
#shutil.move → file ko new folder me shift karta hai            shutil.move(file_path, folder_path)
            print(f"Moved {file} to {folder_name}")











