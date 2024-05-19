import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Завантаження навченої моделі
model = load_model('color_classification_model.h5')

# Функція для передбачення кольору за зображенням
def predict_color(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    color_classes = ['Red', 'Green', 'Blue']
    # Змініть порядок класів, якщо вони не відповідають вашому набору даних
    predicted_color = color_classes[np.argmax(prediction)]
    return predicted_color

# Шлях до зображення, яке ви хочете класифікувати
image_path = '1.jpg'

# Отримання передбачення
predicted_color = predict_color(image_path)
print('Predicted color:', predicted_color)
