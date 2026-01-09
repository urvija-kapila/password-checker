import secrets
import string

def generate_password(length=16):
    if length < 12:
        length = 12  # enforce minimum secure length

    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
