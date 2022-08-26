from Encoder import Encrypt
from Decoder import Decrypt
if __name__ == "__main__":

    
    Input = input("for Encryption press 'E' and for Decryption press 'D'\n  :------>  ")
    check=(Input[:1:].lower())
    
    if check == "e":
        Encrypt()
    elif check == "d": 
        Decrypt()
