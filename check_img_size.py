import os
from PIL import Image


folder_path = "/home/ubuntu/Workspace/phat-intern-dev/VinAI/mvsplat/input_view/view_1"

for filename in os.listdir(folder_path):
    if filename.endswith('.png') or filename.endswith('.jpeg'):
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        print(f"Image {filename} has size {img.size}.")
