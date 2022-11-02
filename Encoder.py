from ast import Not
from encodings import utf_8
import os
import time
from cryptography.fernet import Fernet
import datetime
from loading import loading


def Encrypt ():
    os.system("clear")
    os.system("color 04")
    key = Fernet.generate_key()
    key2=Fernet.generate_key()
    key3=str(key2)
    key_req1=(key3.replace("b'",''))
    key_req=(key_req1.replace("'",'')) 
    Fernet_key = Fernet(key)
    enc_message = input("\n Enter string for Encryption\n  :------> ")
    print("\n Enter strong key , suggest key ----> ",key_req )
    enc_message_1=input("  :------> ")
    enc ="!@$#$*#$*_)*#$()&$+_NJ&*@&i98324^$@!(*#!_)#_+!*#!$*DesTRoYerIG%@64!$#|\;$@$"
    enc_DB=enc+enc_message_1 

    encMessage = Fernet_key.encrypt(enc_message.encode())
    encMessage1 = Fernet_key.encrypt(enc_message_1.encode())
    enc1 = Fernet_key.encrypt(enc.encode())
    enc2 = Fernet_key.encrypt(enc_DB.encode())
    Message1_0=str(encMessage)
    Message1_1=Message1_0.replace("b'",'')
    Message1=Message1_1.replace("'",'')
    Message2_0=str(encMessage1)
    Message2=Message2_0.replace("b'",'')
    Message3=Message1[:30]+Message2+Message1[30:]
    com_encMessage=(bytes((Message3),'utf8'))
    
    Encrypt_String = com_encMessage+ encMessage1 + enc1 + enc2
 
  

    if enc_message:
        loading()
        os.system("clear")
        os.system("color 02")


    print("\n Encrypted string\n  :------>\n\n",Encrypt_String,"  ")
    print("\n Auto generated KEY\n  :------>\n\n",encMessage1,"  ")
    print("\n Encrypted KEY (main)\n  :------>\n\n ",key,"  ")
    print("\n Encrypt Number  :------> ",(len(encMessage)))
    print("\n Encrypted string length  :------> ",(len(Encrypt_String)-1))
    f = open("DESTROYER_Encode.txt", "a")
    today = datetime.datetime.now()
    f.write(" Created ~~]:==------->  "+str(today) +"\n\nEncrypted string  :------>  "+str(Encrypt_String)+"\nAuto generated KEY  :------> "+str(encMessage1)+"\nEncrypted KEY (main)     :------> "+str(key)+"\nEncrypt Number    :------> "+str(len(encMessage))+"\nEncrypted str length:-----> "+str(len(Encrypt_String))+"\n\n\n\n")
    f.close()
    print("\n Encode text saved in DESTROYER_Encode.txt")

