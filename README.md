🌿 Plant Disease Detection System

A web-based Plant Disease Detection System that uses Machine Learning and Deep Learning to identify plant diseases from leaf images. Users can upload an image of a plant leaf through the web application, and the trained model predicts the corresponding disease.

The system provides a simple and user-friendly interface for image-based disease detection along with user authentication and prediction history.

📌 Project Overview

Plant diseases can significantly affect crop quality and agricultural productivity. Early identification of diseases can help in taking appropriate preventive and corrective measures.

This project provides a web-based solution where a user can:

Register or log in to the system.
Upload an image of a plant leaf.
Process the image through a trained Machine Learning model.
Get the predicted plant disease.
View previous prediction records through the history section.

The application combines a Flask-based web interface with a trained Keras deep learning model to provide automated plant disease detection.

✨ Key Features
🌱 Plant Disease Detection
Predicts plant diseases from uploaded leaf images.
📷 Image Upload
Allows users to upload plant leaf images for prediction.
🤖 Machine Learning Model
Uses a trained Keras/TensorFlow model for image classification.
🔐 User Authentication
Provides registration and login functionality.
📊 Prediction History
Allows users to view their previous disease detection results.
🖥️ Web-Based Interface
Simple and user-friendly interface accessible through a web browser.
📱 Responsive Design
Designed to provide a convenient experience across different screen sizes.
🛠️ Technologies Used
Technology	Purpose
Python	Backend programming
Flask	Web application framework
TensorFlow / Keras	Deep learning model
HTML5	Web page structure
CSS3	Styling and user interface
JavaScript	Client-side functionality
Git & GitHub	Version control and project management
🧠 Machine Learning

The system uses a trained deep learning image classification model to recognize plant diseases from leaf images.

Prediction Workflow
Plant Leaf Image
       ↓
   Image Upload
       ↓
 Image Preprocessing
       ↓
 Trained ML Model
       ↓
 Disease Classification
       ↓
 Predicted Disease
       ↓
 Display Result

The trained model is stored as:

Plant_Disease_Model.keras
🌾 Dataset

The project uses a plant leaf image dataset containing different plant species and disease categories.

The dataset contains separate folders representing different disease classes, including examples such as:

Apple diseases
Corn/Maize diseases
Pepper diseases
Potato diseases
Tomato diseases
Dataset Availability

The complete dataset is not included in this GitHub repository because of its large size.

The dataset is kept locally and is excluded using .gitignore.

Dataset/
🖥️ Application Pages
🏠 Home

The home page provides an introduction to the Plant Disease Detection System and allows users to access the detection functionality.

🔐 Login & Registration

Users can create an account and securely log in to access the application.

🌿 Disease Detection

Users can upload a plant leaf image and receive the predicted disease from the trained model.

📜 Prediction History

Users can view their previous disease detection results.

ℹ️ About

Provides information about the project and its purpose.

📂 Project Structure
Plant_Disease/
│
├── app.py
├── model.py
├── Plant_Disease_Model.keras
├── .gitignore
├── README.md
│
├── static/
│   ├── plant_bg.jpg
│   ├── style.css
│   └── uploads/
│       ├── corn_rust_disease.png
│       └── Tips for growing disease-free tomatoes.jpg
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── history.html
│   └── about.html
│
└── Dataset/                 # Excluded from GitHub

