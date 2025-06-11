# ThreatSniffer 🛡️

ThreatSniffer is a lightweight Flask web application that detects potential phishing emails using a trained machine learning model. Just paste an email's full content (including headers), and ThreatSniffer will classify it as either **legitimate** or **phishing**.

---

## 🔍 Features

- 🚨 Detects phishing indicators in both headers and body of emails
- 🔬 Extracts features like suspicious domains, keywords, and suspicious links
- 🧠 Uses a pre-trained machine learning model to classify email content
- 🌐 Simple web interface to test email content
- 📊 Easily extendable with new features and models

---

## 📁 Project Structure
```
ThreatSniffer/
├── app.py                      
├── model/
│   └── phishing_detector_model.pkl  
├── utils/
│   └── feature_extractor.py    
├── templates/
│   └── index.html              
└── README.md                   


```
---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/yourusername/ThreatSniffer.git
cd ThreatSniffer
```

### 2. Create and activate a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install the required packages
```
pip install -r requirements.txt
```

### 4. Add the trained model
Ensure your trained model file is saved as:

```model/phishing_detector_model.pkl
(You'll need to training it.)
```

---

### 🚀 Run the App
```
python app.py
Visit http://127.0.0.1:5000 in your browser.
```

### 🧪 Example Input
Paste a full raw email, like:

```
From: suspicious@badsite.ru
Subject: Please verify your login
Received: None

Dear user,

Please verify your login at http://malicious-site.com

Regards,
Fake Support
The app will classify it as phishing or legitimate.
```

### 🧠 Model Training (optional)
If you want to train your own model:

Collect a dataset of phishing and legitimate emails

Extract features using the same logic in utils/feature_extractor.py

Train with scikit-learn or similar

Save the model using joblib

### 📌 Requirements
Python 3.7+

Flask

scikit-learn

joblib

📄 License
MIT License. Feel free to use, modify, and distribute this project for educational and commercial purposes.

### 🙌 Acknowledgments
Email datasets from open phishing corpora

Python, Flask, and scikit-learn communities



---








