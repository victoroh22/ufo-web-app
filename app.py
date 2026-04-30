import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("./ufo-model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Use float to handle decimal coordinates and match model training
    int_features = [float(x) for x in request.form.values()]
    final_features = pd.DataFrame([int_features], columns=['Seconds', 'Latitude', 'Longitude'])
    prediction = model.predict(final_features)

    output = prediction[0]
    countries = ["Australia", "Canada", "Germany", "UK", "US"]

    return render_template(
        "index.html", prediction_text="Likely country: {}".format(countries[output])
    )

if __name__ == "__main__":
    app.run(debug=True)