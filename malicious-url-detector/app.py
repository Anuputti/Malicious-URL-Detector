from flask import Flask, request, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

os.chdir('C:/Users/chand/OneDrive/Desktop/vscodepojects/DSATM_HACK/malicious-url-detector')
# Correct path to the model file
model_path = "model/malicious_url_detector.pkl"
model = joblib.load(model_path)

# Feature extraction function
def extract_features(url):
    features = {}
    features['length'] = len(url)
    features['num_dots'] = url.count('.')
    features['num_slashes'] = url.count('/')
    # Add more feature extraction as needed
    return features

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = extract_features(url)
    features_df = pd.DataFrame([features])
    prediction = model.predict(features_df)[0]
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
