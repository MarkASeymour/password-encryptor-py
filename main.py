
import os

import Main.application as app
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet



def hash_password(password_provided):
    password = password_provided.encode()
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    hashed = kdf.derive(password)
    key = base64.urlsafe_b64encode(hashed)
    return key

def encrypt_password(password_to_encrypt, key):
    pword = password_to_encrypt.encode()
    f = Fernet(key)
    encrypted = f.encrypt(pword)
    return encrypted


if __name__ == '__main__':
    a = app.greetings()
    key = hash_password(a)
    pword_to_encrypt = input('Enter a password to encrypt: ')
    pword_encrypted = encrypt_password(pword_to_encrypt, key)
    print(f'your password encrypted it: {pword_encrypted}')


