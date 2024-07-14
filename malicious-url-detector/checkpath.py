import joblib
import os
from sklearn.ensemble import RandomForestClassifier

# Sample code to train a model (use your actual model training code here)

# Example model training code
model = RandomForestClassifier()
# Assuming X_train and y_train are your training data
# model.fit(X_train, y_train)

# Ensure the 'model' directory exists
os.makedirs('C:/Users/chand/OneDrive/Desktop/vscodepojects/DSATM_HACK/malicious-url-detector/model', exist_ok=True)

# Save the trained model to the 'model' directory
model_path = 'C:/Users/chand/OneDrive/Desktop/vscodepojects/DSATM_HACK/malicious-url-detector/model/malicious_url_detector.pkl'
joblib.dump(model, model_path)
