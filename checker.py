import math
import string

def password_strength(password):
    score = 0
    remarks = []

    # Length check
    length = len(password)
    if length >= 12:
        score += 25
    elif length >= 10:
        score += 20
    elif length >= 8:
        score += 15
    else:
        remarks.append("Use at least 12 characters.")

    # Uppercase / Lowercase
    if any(c.islower() for c in password):
        score += 10
    else:
        remarks.append("Include lowercase letters.")

    if any(c.isupper() for c in password):
        score += 10
    else:
        remarks.append("Include uppercase letters.")

    # Digits
    if any(c.isdigit() for c in password):
        score += 15
    else:
        remarks.append("Include numbers.")

    # Special characters
    special = string.punctuation
    if any(c in special for c in password):
        score += 15
    else:
        remarks.append("Add special characters (@,#,$,!,%).")

    # Entropy formula
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in special for c in password): charset += len(special)

    entropy = round(len(password) * math.log2(charset)) if charset else 0

    return score, entropy, remarks
