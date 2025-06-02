import re

def mask_pii(text):
    entities = []

    # Email masking
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    for match in re.finditer(email_pattern, text):
        entities.append({
            "position": [match.start(), match.end()],
            "classification": "email",
            "entity": match.group()
        })
    text = re.sub(email_pattern, "[email]", text)

    # Phone number masking (10-digit)
    phone_pattern = r"\b\d{10}\b"
    for match in re.finditer(phone_pattern, text):
        entities.append({
            "position": [match.start(), match.end()],
            "classification": "phone_number",
            "entity": match.group()
        })
    text = re.sub(phone_pattern, "[phone_number]", text)

    return text, entities
