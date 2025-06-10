from flask import Flask, render_template, request
import joblib
from utils.feature_extractor import extract_features  

app = Flask(__name__)

model = joblib.load('model/phishing_detector_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        email_text = request.form.get('email_text')
        if email_text:
          
            parts = email_text.split('\n\n', 1)
            headers_raw = parts[0]
            body = parts[1] if len(parts) > 1 else ""

            headers = {}
            for line in headers_raw.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    headers[key.strip().lower()] = value.strip()

            features = extract_features(headers, body)
            prediction = model.predict([features])[0]
            result = "🚨 Phishing Email Detected" if prediction == 1 else "✅ Legitimate Email"
        else:
            result = "⚠️ Please paste the email content."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
