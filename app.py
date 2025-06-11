from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from keras.models import load_model


app = Flask(__name__)
model = load_model("wine.h5")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        fields = [
            "fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar",
            "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density",
            "pH", "sulphates", "alcohol", "quality"
        ]
        data = [float(request.form[field]) for field in fields]
        prediction = model.predict(np.array([data]))[0][0]
        result = "Red Wine 🍷" if prediction >= 0.5 else "White Wine 🥂"
        return render_template("index.html", prediction=result)
    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")
    
if __name__ == '__main__':
    app.run(debug=True)
