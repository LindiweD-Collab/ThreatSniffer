import joblib
import numpy as np
import sys

def extract_features(url):
    features = [
        len(url),
        url.count('@'),
        url.count('https://'),
        url.count('http://'),
        url.count('-'),
        url.count('.'),
        1 if '//' in url else 0,
        1 if 'login' in url.lower() else 0,
        1 if 'secure' in url.lower() else 0,
    ]
    return np.array(features).reshape(1, -1)

try:
    model = joblib.load('phishing_detector_model.pkl')
except FileNotFoundError:
    print("❌ Model file not found. Please ensure 'phishing_detector_model.pkl' is in the correct folder.")
    sys.exit(1)

url = input("Enter a URL to check: ").strip()
if not url:
    print("❌ No URL entered. Exiting.")
    sys.exit(1)

features = extract_features(url)
prediction = model.predict(features)

if prediction[0] == 1:
    print("⚠️ This URL is likely a phishing site.")
else:
    print("✅ This URL looks safe.")

