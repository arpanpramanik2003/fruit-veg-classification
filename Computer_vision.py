import cv2
import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.efficientnet import preprocess_input
from PIL import ImageFont, ImageDraw, Image

# Load trained EfficientNet model
model = tf.keras.models.load_model('efficient_model.h5')

# Class labels
class_labels = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage',
                'capsicum', 'carrot', 'cauliflower', 'chilli pepper',
                'corn', 'cucumber', 'eggplant', 'garlic', 'ginger',
                'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce',
                'mango', 'onion', 'orange', 'paprika', 'pear',
                'peas', 'pineapple', 'pomegranate', 'potato',
                'raddish', 'soy beans', 'spinach', 'sweetcorn',
                'sweetpotato', 'tomato', 'turnip', 'watermelon']

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.resize(frame, (224, 224))
    img_array = np.expand_dims(img, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions)

    label = f"{class_labels[predicted_class]}: {confidence:.2%}"

    cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Fruit & Vegetable Classifier', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
