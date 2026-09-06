# 🌿 Plant Disease Detection Using Leaf Images

A web-based Deep Learning application that detects plant diseases from leaf images using a trained TensorFlow/Keras image classification model.

---

## 📌 Overview

Plant diseases are one of the major factors affecting crop health, agricultural productivity, and food quality. Early identification of plant diseases can help in taking appropriate preventive measures.

**Plant Disease Detection Using Leaf Images** is a web-based application that uses **Deep Learning and Image Classification** to identify plant diseases from uploaded leaf images.

The user can upload a plant leaf image through the web interface, and the trained model analyzes the image and predicts the corresponding disease category.

The application also provides **user registration, login, and prediction history**, making it a complete web-based disease detection system.

---

## 🎯 Objectives

- Develop an automated plant disease detection system using Deep Learning.
- Detect diseases from plant leaf images.
- Provide a simple and user-friendly web interface.
- Integrate a trained TensorFlow/Keras model with a Flask application.
- Provide user registration and login functionality.
- Maintain prediction history for users.
- Demonstrate the practical application of Artificial Intelligence in agriculture.

---

## 💡 Problem Statement

Traditional plant disease identification often depends on manual visual inspection and expert knowledge. This process can be time-consuming and may not always provide accurate results.

This project aims to provide an automated image-based approach where a user can upload a plant leaf image and obtain a disease prediction using a trained Deep Learning model.

### Basic Workflow

**Leaf Image → Image Processing → Deep Learning Model → Disease Prediction → Result**

---

## 🚀 Key Features

### 🌱 Plant Disease Detection

Users can upload a plant leaf image and receive a predicted disease category using the trained Deep Learning model.

### 📷 Image Upload

The application provides an easy-to-use interface for uploading leaf images.

### 🤖 Deep Learning Prediction

The uploaded image is processed and passed to the trained TensorFlow/Keras model for classification.

### 🔐 User Registration

New users can create an account through the registration page.

### 🔑 User Login

Registered users can securely access the application through the login page.

### 📜 Prediction History

Users can view their previous disease detection results through the history page.

### 🖥️ Web-Based Interface

The model is integrated with a Flask web application, allowing users to interact with the system through a browser.

### ℹ️ About Page

The application includes an About page describing the project and its purpose.

---

# 🧠 How the System Works

The system follows the workflow below:

```text
                    ┌──────────────────┐
                    │       User       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Web Interface  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Upload Leaf Image│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Image Processing │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Deep Learning    │
                    │ Model            │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Disease          │
                    │ Classification   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Prediction Result│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Prediction       │
                    │ History          │
                    └──────────────────┘
```

---

# 🧪 Machine Learning Component

The core of the application is a trained **Deep Learning image classification model**.

The trained model is stored in:

```text
Plant_Disease_Model.keras
```

When a user uploads a leaf image, the application:

1. Receives the uploaded image.
2. Processes the image into the required format.
3. Passes the processed image to the trained model.
4. Performs image classification.
5. Identifies the predicted disease category.
6. Displays the prediction to the user.
7. Stores the prediction in the user's history.

### Prediction Pipeline

```text
Input Leaf Image
       ↓
Image Preprocessing
       ↓
Model Input
       ↓
Deep Learning Model
       ↓
Classification
       ↓
Predicted Disease
       ↓
Result Display
```

---

# 🌾 Dataset

The project uses a plant leaf image dataset containing multiple plant species and disease categories.

The dataset includes plants such as:

- 🍎 Apple
- 🌽 Corn / Maize
- 🌶️ Pepper
- 🥔 Potato
- 🍅 Tomato

Examples of disease categories include:

```text
Apple___Apple_scab
Apple___Black_rot
Apple___Cedar_apple_rust
Apple___healthy

Corn_(maize)___Cercospora_leaf_spot
Corn_(maize)___Common_rust
Corn_(maize)___healthy
Corn_(maize)___Northern_Leaf_Blight

Pepper,_bell___Bacterial_spot
Pepper,_bell___healthy

Potato___Early_blight
Potato___healthy
Potato___Late_blight

Tomato___Bacterial_spot
Tomato___Early_blight
Tomato___healthy
Tomato___Late_blight
Tomato___Leaf_Mold
Tomato___Septoria_leaf_spot
Tomato___Spider_mites
Tomato___Target_Spot
Tomato___Tomato_mosaic_virus
Tomato___Tomato_Yellow_Leaf_Curl_Virus
```

### Dataset Availability

The complete dataset is **not included in this GitHub repository** because of its large size.

The dataset is excluded from Git tracking using `.gitignore`:

```gitignore
Dataset/
```

This keeps the GitHub repository lightweight while allowing the dataset to remain available in the local development environment.

---

# 🖥️ Application Pages

## 🏠 Home Page

Provides the main interface and access to the plant disease detection functionality.

## 🔐 Login Page

Allows registered users to log in to the application.

## 📝 Registration Page

Allows new users to create an account.

## 🌿 Disease Detection

Users upload a plant leaf image and receive the predicted disease.

## 📜 Prediction History

Displays previously generated disease prediction results for the user.

## ℹ️ About Page

Provides information about the project, its purpose, and the technologies used.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Flask** | Web application framework |
| **TensorFlow** | Deep Learning framework |
| **Keras** | Model development and loading |
| **HTML5** | Web page structure |
| **CSS3** | Styling and user interface |
| **JavaScript** | Client-side functionality |
| **Git** | Version control |
| **GitHub** | Source code repository |

---

# 📂 Project Structure

```text
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
│   │
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
└── Dataset/
    └── Excluded from GitHub
```

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/pastelrutu/Plant-Disease-Detection-Using-Leaf-Images.git
```

Navigate to the project directory:

```bash
cd Plant-Disease-Detection-Using-Leaf-Images
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the required Python libraries used by the project.

---

## 5. Run the Application

Start the Flask application:

```bash
python app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

# 🔄 Application Workflow

```text
User Registration
       ↓
User Login
       ↓
Home Page
       ↓
Upload Leaf Image
       ↓
Image Processing
       ↓
Deep Learning Prediction
       ↓
Disease Result
       ↓
Prediction Stored
       ↓
View Prediction History
```

---

# 🔐 Data and Repository Management

Large datasets and unnecessary development files are excluded from GitHub using `.gitignore`.

Examples include:

```text
Dataset/
venv/
.venv/
__pycache__/
*.pyc
.env
.vscode/
.ipynb_checkpoints/
```

This helps keep the repository clean and prevents large datasets or environment-specific files from being uploaded.

---

# 📊 Example Predictions

### Example 1

```text
Input:
Tomato Leaf Image

        ↓

Model Prediction

        ↓

Tomato___Late_blight
```

### Example 2

```text
Input:
Corn Leaf Image

        ↓

Model Prediction

        ↓

Corn_(maize)___Common_rust
```

The predicted disease category is then displayed through the web application.

---

# 🔒 Security Considerations

The application provides basic user authentication through registration and login functionality.

Sensitive configuration files such as:

```text
.env
```

are excluded from version control.

For production deployment, additional security measures such as secure password hashing, session management, input validation, HTTPS, and secure database configuration should be implemented.

---

# 🚧 Limitations

- Prediction performance depends on the quality of the uploaded image.
- The model can classify only the disease categories it was trained on.
- The complete dataset is not included in the GitHub repository because of its size.
- The application is primarily intended for educational and demonstration purposes.
- Real-world deployment would require testing with diverse field images and environmental conditions.

---

# 🔮 Future Enhancements

The system can be further improved by adding:

### 📱 Mobile Application

Develop an Android/iOS application for convenient mobile-based disease detection.

### ☁️ Cloud Deployment

Deploy the application to a cloud platform for remote access.

### 🌍 More Plant Species

Expand the model to support additional crops and disease categories.

### 🎯 Improved Model Performance

Experiment with advanced CNN architectures, transfer learning, and data augmentation.

### 💊 Treatment Recommendations

Provide possible prevention and treatment recommendations along with the detected disease.

### 🌐 Multilingual Support

Add multiple languages to make the application more accessible to users.

### 📈 Analytics Dashboard

Provide visual analytics for disease predictions and historical trends.

### 📷 Real-Time Detection

Integrate camera-based detection for real-time leaf disease analysis.

---

# 🎓 Educational Purpose

This project demonstrates the integration of:

```text
Machine Learning
       +
Deep Learning
       +
Image Classification
       +
Python
       +
Flask
       +
Web Development
       +
Git & GitHub
```

It provides a practical example of integrating an AI/ML model into a web application to address an agriculture-related problem.

---

# 📌 Project Highlights

| Component | Details |
|---|---|
| **Project Type** | Web Application |
| **Domain** | Agriculture / Artificial Intelligence |
| **Machine Learning Task** | Image Classification |
| **Model Format** | Keras |
| **Backend** | Flask |
| **Programming Language** | Python |
| **Frontend** | HTML, CSS, JavaScript |
| **Authentication** | Login & Registration |
| **History** | Prediction History |
| **Dataset** | Plant Leaf Images |
| **Version Control** | Git |
| **Repository** | GitHub |

---

# 🌱 Conclusion

The **Plant Disease Detection Using Leaf Images** system demonstrates how Deep Learning can be integrated with a web application to provide an automated approach to plant disease identification.

By allowing users to upload leaf images and receive model-based predictions through a simple web interface, the project demonstrates the practical application of Artificial Intelligence in agriculture.

The system provides a foundation that can be further extended with additional plant species, improved models, treatment recommendations, mobile support, analytics, and cloud deployment.

---

# 📜 License

This project is developed for **educational and academic purposes**.

---

# 👨‍💻 Project Information

**Project Title:**  
Plant Disease Detection Using Leaf Images

**Domain:**  
Artificial Intelligence / Machine Learning / Agriculture

**Technologies:**  
Python, Flask, TensorFlow, Keras, HTML, CSS, JavaScript

---

## ⭐ Acknowledgement

This project was developed as part of an **internship project** to explore the practical implementation of Machine Learning, Deep Learning, and Web Development in the agricultural domain.

---

⭐ **If you find this project useful, consider giving the repository a star!**

---
## Author
RUTUJA MESHRAM
