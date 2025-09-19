from password_utils_decrypt import encrypt_password
from cryptography.fernet import Fernet

def generate_key():
    key=Fernet.generate_key()
    #print(key)
    with open("secret.key","wb")as f:
        f.write(key)
    print("\033[33m Key was successfully writed in the secret file...")

if __name__ == "__main__":

    generate_key()

    get_password = input("\033[31m Enter the password to encrypt (Masking): ")

    #encrypted = encrypt_password("nandhu")
    encrypted = encrypt_password(get_password)

    print("\033[33m Encrypted password apply it on 'password_utils_decrypt' ")
    print(f"\033[36m{encrypted}\033[0m")

