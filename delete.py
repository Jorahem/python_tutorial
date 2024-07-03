import os
import hashlib
import imagehash
from PIL import Image

# Specify the folder path
folder_path = 'E:\picture\Screenshots'

# List of common image and video file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']

# Function to calculate file hash
def calculate_file_hash(file_path, is_image):
    hash_algo = hashlib.md5()
    if is_image:
        # Use image hash for images
        image = Image.open(file_path)
        image_hash = imagehash.average_hash(image)
        return str(image_hash)
    else:
        # Use md5 hash for videos
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()

# Function to delete duplicate files
def delete_duplicates(folder, extensions, is_image=False):
    file_hashes = {}
    for root, _, files in os.walk(folder):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                file_hash = calculate_file_hash(file_path, is_image)
                if file_hash in file_hashes:
                    try:
                        os.remove(file_path)
                        print(f"Deleted duplicate: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")
                else:
                    file_hashes[file_hash] = file_path

# Delete duplicate image files
delete_duplicates(folder_path, image_extensions, is_image=True)

# Delete duplicate video files
delete_duplicates(folder_path, video_extensions, is_image=False)

print("Duplicate deletion process completed.")
