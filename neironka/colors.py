from PIL import Image
import os

# Створення піддиректорій для кольорів
colors = ['red', 'green', 'blue']
base_dir = 'color_classification_dataset'

for color in colors:
    os.makedirs(os.path.join(base_dir, color), exist_ok=True)

# Створення та збереження зображень кольорів
image_size = (100, 100)
for color in colors:
    # Створення зображення потрібного кольору
    image = Image.new('RGB', image_size, color)
    # Збереження зображення
    image.save(os.path.join(base_dir, color, f'{color}.jpg'))