# Fruits & Vegetables Classification 🍎🥕🍉🥭

[Dataset Link](https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition)

## 📌 Project Overview
This project is a **deep learning-based image classification system** that identifies different types of fruits and vegetables from an uploaded image. The model is built using **TensorFlow** and deployed using **Streamlit**.

## 🖥️ Tech Stack
- **Python** (Core programming language)
- **TensorFlow/Keras** (For model training and inference)
- **Streamlit** (For building the web UI)
- **NumPy & PIL** (For image preprocessing)
- **Matplotlib** (For visualization)

## 🎯 Features
- Upload an image of a fruit or vegetable
- Predict the class with confidence score
- Display confidence scores as a bar chart
- User-friendly and interactive interface

## 🏗️ Project Structure
```
fruit_veg_classifier/
├── cnn_model.h5           # Trained CNN model
│── app.py                 # Streamlit web app script
│── requirements.txt       # Dependencies for the project
│── README.md              # Project documentation
```

## 🚀 Installation & Usage
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/arpanpramanik2003/fruit-veg-detection-custom-CNN.git
cd fruit-veg-detection-custom-CNN
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```sh
streamlit run app.py
```

## 📷 Model & Image Preprocessing
- The model is a **CNN-based classifier** trained on a dataset of fruits and vegetables.
- Input images are resized to **224x224 pixels** before inference.

## 📊 Prediction Output
- **Class Label:** Name of the detected fruit/vegetable
- **Confidence Score:** Probability of prediction accuracy
- **Bar Chart:** Visualization of class probabilities

## 🛠️ Future Improvements
- Improve accuracy with advanced architectures (ResNet, MobileNetV2)
- Deploy on cloud platforms like **Render/Streamlit Cloud**
- Add more dataset classes for better generalization

## 📜 License
This project is open-source and available under the **MIT License**.

---
📌 **Developed by Arpan Pramanik** | 💡 AI/ML Enthusiast 🚀

