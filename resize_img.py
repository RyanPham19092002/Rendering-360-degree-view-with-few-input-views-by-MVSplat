import os
from PIL import Image

folder_path = "/home/ubuntu/Workspace/phat-intern-dev/VinAI/mvsplat/input_view/view_1"

for filename in os.listdir(folder_path):
    if filename.endswith('.png') or filename.endswith('.jpeg'):
        file_path = os.path.join(folder_path, filename)
        print(file_path)
        img = Image.open(file_path)
        new_img = img.resize((256, 256))
        new_img.save(file_path)
        print(f"Resized image {filename} in {folder_path} successfully.")
