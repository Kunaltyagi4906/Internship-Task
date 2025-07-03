import os
from PIL import Image


input_folder = "images"
output_folder = "resized_images"
target_size = (300, 300)  

# create output folder if by chance not created
os.makedirs(output_folder, exist_ok=True)
if not os.path.exists(input_folder):
    print(f"Folder not found: {input_folder}")
    exit()

#sabhi input inamges ke liye loop
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

      
        img_resized = img.resize(target_size)

        save_path = os.path.join(output_folder, filename)
        img_resized.save(save_path)

        print(f" {filename} resized and saved to {save_path}")

print("\n All images resized successfully!")
