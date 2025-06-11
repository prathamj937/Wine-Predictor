# Wine-Predictor

🍷 Wine Type Prediction Web App

A simple Flask-based web application to predict whether a wine is Red Wine 🍷 or White Wine 🥂 based on 12 physicochemical input features using a pre-trained machine learning model (wine_model.h5) trained on the UCI Wine Quality Dataset.

# 🚀 Features:

1. Input 12 wine characteristics via a user-friendly form

2. Predicts wine type (Red or White) in real-time

3. Clean and minimal UI with Jinja templating

4. Built with Flask and TensorFlow/Keras for robust performance

# 🧠 Model Input Features
The model uses the following 12 features to make predictions:

1. Fixed Acidity (g/L)
2. Volatile Acidity (g/L)
3. Citric Acid (g/L)
4. Residual Sugar (g/L)
5. Chlorides (g/L)
6. Free Sulfur Dioxide (mg/L)
7. Total Sulfur Dioxide (mg/L)
8. Density (g/cm³)
9. pH
10. Sulphates (g/L)
11. Alcohol (% vol.)
12. Quality (score from 0–10)

# 🛠️ Tech Stack

Python: Core programming language
Flask: Web framework for serving the app
TensorFlow/Keras: Machine learning model for predictions
HTML/Jinja: Frontend templating for the user interface
NumPy: Data processing for model inputs

# 📁 Folder Structure

wine-predictor/
├── app.py                # Flask application
├── wine_model.h5         # Pre-trained ML model
├── requirements.txt       # Python dependencies
└── templates/
    └── index.html        # Frontend form

# ⚙️ Setup Instructions

Follow these steps to set up and run the application locally:

1. ✅ Clone the Repository

git clone https://github.com/your-username/wine-predictor.git
cd wine-predictor

2. 🐍 Create and Activate a Virtual Environment (Recommended)

python -m venv venv
# For Windows
venv\Scripts\activate
# For Mac/Linux
source venv/bin/activate

3. 📦 Install Dependencies

pip install flask tensorflow keras numpy 

4. 🔮 Ensure Model Exists

Ensure wine.h5 is in the project root. If you need to train and save a new model, use:

model.save("wine_model.h5")

5. 🧪 Run the Application

python app.py

6. 🌐 Access the App

Open your browser and navigate to http://127.0.0.1:5000.
