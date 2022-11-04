# chat_client.py
import sys, socket, select, os, base64, getpass, time
import ssl
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from mk_cert_files import *

#Own modules
from SSLUtil import *

def chat_client(password):
    #Create a password for the signature private key
    if password == None:
        while 1:
            password = getpass.getpass("Enter a password for your private key>")
            password_check = getpass.getpass("Enter it again>")
            if password == password_check:
                break
            else:
                print("Passwords does not match.")
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    sk = kdf.derive(password.encode('UTF-8'))
    done = False
    try:
        while done == False:
            print("Define action: \n1. Recover key. \n:q to quit.")
            action = input(">")
            if action.lower() == ":q":
                sys.exit()

            if action == "1":
                # TODO the actual project
                print("enter password guess")
                password_guess = input()
                recovered_sk = "peoplecantry".encode('UTF-8')
                if recovered_sk == sk:
                    print("recovered correctly!")
                else:
                    print("u clown")
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    sys.exit(chat_client(None))
