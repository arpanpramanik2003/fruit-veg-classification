import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.keras.applications.efficientnet import preprocess_input

# Load the trained model
model = tf.keras.models.load_model('efficient_model.h5')

# Define class labels
class_labels = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage',
                'capsicum', 'carrot', 'cauliflower', 'chilli pepper',
                'corn', 'cucumber', 'eggplant', 'garlic', 'ginger',
                'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce',
                'mango', 'onion', 'orange', 'paprika', 'pear',
                'peas', 'pineapple', 'pomegranate', 'potato',
                'raddish', 'soy beans', 'spinach', 'sweetcorn',
                'sweetpotato', 'tomato', 'turnip', 'watermelon']

# Streamlit UI
st.set_page_config(page_title="Fruit & Veg Classifier", layout="centered")
st.title("🍎🥕 Fruits & Vegetables Classification 🍉🥭")
st.write("Upload an image of a fruit or vegetable, and the model will classify it!")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image)  
    image = preprocess_input(image)  
    image = np.expand_dims(image, axis=0)
    return image

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Center the image using Streamlit columns
    col1, col2, col3 = st.columns([1, 2, 1])  # Middle column is wider
    with col2:
        st.image(image, caption="Uploaded Image", use_container_width=True)  

    # Preprocess the image
    processed_image = preprocess_image(image)

    # Make predictions
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions)

    # Display results
    st.subheader("🔍 Prediction Results")
    st.write(f"**Class:** {class_labels[predicted_class].capitalize()}")  # Capitalize the first letter
    st.write(f"**Confidence:** {confidence:.2%}")

    # Confidence bar
    st.progress(int(confidence * 100))

    # Show class probabilities as a bar chart
    fig, ax = plt.subplots()
    ax.bar(class_labels, predictions[0], color='skyblue')
    plt.xticks(rotation=90, fontsize=8)
    plt.ylabel("Confidence")
    plt.title("Class Probabilities")
    st.pyplot(fig)

st.markdown("---")
st.write("📌 Built with Streamlit & TensorFlow")
st.write("Arpan Pramanik")
