"""This program is a simple login program that will ask the user for a username and password. I will be attached to
the main program later on """

from cryptography import fernet as fer

import m

"""
with open("key.key", "rb") as key_file:
    key = key_file.read()
    fernet = cry.Fernet(key)
    with open("passwords.txt", "rb") as file:
        encrypted = file.read()
        decrypted = fernet.decrypt(encrypted)
        print(decrypted)
        print(pickle.loads(decrypted))
"""
a = fer.Fernet.generate_key()


