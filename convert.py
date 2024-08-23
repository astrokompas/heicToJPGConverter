import os
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()

def convert(heic_path, jpg_path):
    try:
        image = Image.open(heic_path)
        image.save(jpg_path, "JPEG")
        print(f"Converted {heic_path} to {jpg_path}")
    except Exception as e:
        print(f"Failed to convert {heic_path}: {e}")

def convertAndDelete(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    files = os.listdir(directory)
    if not files:
        print(f"No files found in directory '{directory}'.")
        return
    
    print(f"Found {len(files)} files in directory '{directory}'.")
    
    for filename in files:
        if filename.lower().endswith(".heic"):
            heic_file_path = os.path.join(directory, filename)
            jpg_file_path = os.path.splitext(heic_file_path)[0] + ".jpg"
            
            print(f"Processing file: {heic_file_path}")

            convert(heic_file_path, jpg_file_path)

            try:
                os.remove(heic_file_path)
                print(f"Deleted {heic_file_path}")
            except Exception as e:
                print(f"Failed to delete {heic_file_path}: {e}")
        else:
            print(f"Skipped non-HEIC file: {filename}")
    
    print("Processing completed.")

directory = "."
convertAndDelete(directory)
