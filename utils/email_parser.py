import email

def parse_email(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        msg = email.message_from_file(f)

    headers = {
        "from": msg.get("From", ""),
        "to": msg.get("To", ""),
        "subject": msg.get("Subject", ""),
        "received": msg.get("Received", "")
    }

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += part.get_payload(decode=True).decode('utf-8', errors='ignore')
    else:
        body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')

    return headers, body
