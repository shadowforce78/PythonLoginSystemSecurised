import os
import simple_chalk as chalk
from cryptography.fernet import Fernet


def decryptUUID():
    if os.name == 'nt':
        uuidFile = 'uuid.txt'
    else:
        uuidFile = '.uuid.txt'
    with open("key.key", "rb") as f:
        key = f.read()
    cipher = Fernet(key)
    with open(f"{uuidFile}", "rb") as f:
        encrypted_uuid = f.read()
    uuid = cipher.decrypt(encrypted_uuid).decode()
    return uuid
