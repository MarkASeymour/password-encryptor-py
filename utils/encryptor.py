import base64
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def hash_password(password_provided):
    password = password_provided.encode()
    salt = ''.encode()
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


def decrypt_password(password_to_decrypt, key):
    f = Fernet(key)
    password_to_decrypt = password_to_decrypt.encode()
    decrypted = f.decrypt(password_to_decrypt)
    return decrypted.decode()
