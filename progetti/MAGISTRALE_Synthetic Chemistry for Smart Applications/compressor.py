import os
from PIL import Image

# Parameters
INPUT_FOLDER = "images"  # Change to your folder
OUTPUT_FOLDER = os.path.join(INPUT_FOLDER, "compressed")
SCALE_FACTOR = 0.75  # Resize to 75% of original size
JPEG_QUALITY = 85  # 85% quality

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Process all JPEG images in the folder
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        # Open image
        with Image.open(input_path) as img:
            # Compute new size
            new_size = (int(img.width * SCALE_FACTOR), int(img.height * SCALE_FACTOR))
            resized_img = img.resize(new_size, Image.LANCZOS)  # Updated filter

            # Save compressed image
            resized_img.save(output_path, "JPEG", quality=JPEG_QUALITY)

            print(f"Processed: {filename} -> {output_path}")

print("All images processed successfully!")
