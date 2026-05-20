from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("xgb_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    lags = []
    for i in range(1, 25):
        val = float(request.form[f'lag_{i}'])
        lags.append(val)

    # Rolling features
    rolling_6 = np.mean(lags[:6])
    rolling_12 = np.mean(lags[:12])

    # Create dataframe
    input_data = pd.DataFrame([lags], columns=[f'lag_{i}' for i in range(1, 25)])
    input_data['rolling_mean_6'] = rolling_6
    input_data['rolling_mean_12'] = rolling_12

    # Align features
    model_features = model.feature_names_in_

    for col in model_features:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[model_features]

    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2),
        past_values=lags
    )

if __name__ == "__main__":
    app.run(debug=True)