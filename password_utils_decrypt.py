from cryptography.fernet import Fernet

class FakeStr(str):
    def __str__(self):
        #return "****"
        return f"\033[35mThe masked password is: \033[0m" + "*" * len(self)
    def __repr__(self):
        #return "$$$$"
        return "The masked password is: " + "~" * len(self)

def load_key():
    return open("secret.key","rb").read()

def encrypt_password(password):
    key=load_key()
    f= Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key=load_key()
    f=Fernet(key)
    decrypted= f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)
    #return decrypted

if __name__ == "__main__":
    def get_decrypted_password():
        encrypt_key = input("\033[31mEnter the encrypted key: \033[0m")
        encrypted_password = encrypt_key
        return  decrypt_password(encrypted_password)


    print( get_decrypted_password())



