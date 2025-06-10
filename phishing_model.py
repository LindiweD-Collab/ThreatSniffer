import pandas as pd
import re
import joblib
import os
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Create model folder
os.makedirs('model', exist_ok=True)

# Fetch dataset
print("📥 Fetching dataset...")
website_phishing = fetch_ucirepo(id=379)

# Load dataset
df = pd.concat([website_phishing.data.features, website_phishing.data.targets], axis=1)

# Rename target column to 'label'
df.rename(columns={'Result': 'label'}, inplace=True)

# Convert label to binary (1 for phishing, 0 for legitimate)
df['label'] = df['label'].apply(lambda x: 1 if x == 1 else 0)

# Combine all columns into synthetic text
df['text'] = df.astype(str).agg(' '.join, axis=1)

# Define feature extractor
def extract_features(email_text):
    email_text = email_text.lower()
    features = {
        'length': len(email_text),
        'num_links': len(re.findall(r'http[s]?://', email_text)),
        'num_login': email_text.count("login"),
        'num_verify': email_text.count("verify"),
        'num_html': email_text.count("<html"),
        'num_account': email_text.count("account"),
        'num_uppercase': sum(1 for c in email_text if c.isupper()),
        'has_suspicious_words': int(any(word in email_text for word in ['paypal', 'bank', 'verify', 'click here', 'urgent', 'immediate action'])),
        'has_spammy_phrases': int(any(phrase in email_text for phrase in ['free', 'winner', 'congratulations', 'claim your prize'])),
        'has_urgent_action': int('urgent' in email_text or 'immediate action' in email_text),
        'has_personal_info': int(any(word in email_text for word in ['social security', 'credit card', 'bank account'])),
        'has_misspelled_words': int(any(word in email_text for word in ['recieve', 'adress', 'seperate', 'definately'])),
        'has_unusual_sender': int('noreply' in email_text or 'admin' in email_text or 'support' in email_text),
        'has_unusual_links': int(any(link in email_text for link in ['bit.ly', 'tinyurl.com', 'goo.gl'])),
        'has_spelling_errors': int(any(word in email_text for word in ['teh', 'recieve', 'definately', 'occured'])),
        'has_phishing_keywords': int(any(keyword in email_text for keyword in ['phishing', 'scam', 'fraud', 'malware'])),
        'has_attachments': int('attachment' in email_text or 'attached' in email_text),
    }
    return list(features.values())

X = df['text'].apply(extract_features).tolist()
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

model_path = 'model/phishing_detector_model.pkl'
joblib.dump(clf, model_path)
print(f"✅ Model saved to '{model_path}'")

