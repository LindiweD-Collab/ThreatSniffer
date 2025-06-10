import re

def extract_features_from_email(msg):
    headers = {
        'from': msg.get('From', ''),
        'to': msg.get('To', ''),
        'subject': msg.get('Subject', ''),
        'received': msg.get('Received', '')
    }

    # Extract body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += part.get_payload(decode=True).decode('utf-8', errors='ignore')
    else:
        body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')

    # Feature vector
    return [
        len(headers['subject'] or ""),
        len(body),
        int(bool(re.search(r'http[s]?://', body))),
        body.lower().count("login"),
        body.lower().count("verify"),
        body.lower().count("bank"),
        int('<html' in body.lower()),
        sum(1 for c in body if c.isupper()),
    ]
