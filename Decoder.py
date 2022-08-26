
from loading import loading

from ast import Not
from encodings import utf_8
import os
from cryptography.fernet import Fernet
import datetime
def Decrypt(): 
    os.system("clear")
    os.system("color 06")
    

    dec_message1 = input("\n Enter Encrypted string\n  :------> ")
    key_auto_0=(input("\n Auto generated KEY          \n   :------> ")) 
    key_0=(input("\n Enter Encrypted KEY (main)  \n  :------> ")) 
    key_auto=key_auto_0.replace("b'",'')
    lenth=int(input("\n Enter Encrypted Number \n  :------> "))
    dec_message=dec_message1.replace(key_auto,"")
    key_1=key_0.replace("b'",'')
    key_2=key_1.replace("'",'') 
    key=bytes(key_2,'utf8')
    Fernet_key = Fernet(key)
    decrm1=dec_message.strip().replace('b"','')
    decrm=decrm1.replace('"','')
    Decrypt=bytes( ((decrm[:lenth:])),'utf8')
    decrypt_string = Fernet_key.decrypt(Decrypt).decode()
    if dec_message1:
        loading()
    os.system("clear")
    os.system("color 02")
    print("\n Original string\n  :------> ",decrypt_string," <------|")
    f = open("DESTROYER_Decode.txt", "a")
    today = datetime.datetime.now()
    f.write(" Created ~~]:==------->  "+str(today) +"\n\nEncrypted string  :------>  "+str(dec_message)+"\nEncrypted KEY (main)     :------> "+str(key_0)+"\nDecrypted string     :------> "+str(decrypt_string)+"\n\n\n\n")
    f.close()
    print("\n saved in DESTROYER_Decode ")

