import re

def extract_features(headers, body):
    features = []

    features.append(1 if "@" in headers.get("from", "") and not headers["from"].endswith(".com") else 0)
    features.append(1 if "Received" not in headers.get("received", "") else 0)
    features.append(len(headers.get("subject", "")))

    features.append(len(body))
    features.append(body.lower().count("login"))
    features.append(body.lower().count("verify"))
    features.append(1 if "http://" in body or "https://" in body else 0)
    features.append(1 if "bank" in body.lower() or "paypal" in body.lower() else 0)

    return features
