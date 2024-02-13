from cryptography.fernet import Fernet
import base64
import hashlib

print("you GET A FLAG LIKE----- bYtE_BuStErS{xxxxxxxxxxxxxxxxx}-----  IF YOU SUCCESSFULL Bruteforced using dictionary.txt\n\n")

key = input("enter the FOUR DIGIT KEY HERE:::")

# Ensure the key is exactly 4 characters long
if len(key) != 4:
    raise ValueError("Key must be exactly 4 characters long\n")




encrypted_data = "[kG}fpFkMwAkBbJLQ]]gPFlK\W^gM]Q]Xm@VXYVE"

decrypted_data = ''.join(chr(ord(encrypted_data[i]) ^ ord(key[i % 4])) for i in range(len(encrypted_data)))

print("Encrypted:", encrypted_data)

print("Decrypted:", decrypted_data)

