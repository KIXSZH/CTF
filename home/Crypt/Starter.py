def xor_encrypt(message, key):
    decrypted = []
    for i in range(len(message)):
        decrypted_char = chr(ord(message[i]) ^ ord(key[i % len(key)]))
        decrypted.append(decrypted_char)
    return ''.join(decrypted)


# Example usage:

decryption_key = "Secret"
'''def Decrypt():
    decrypted_text = xor_encrypt(plaintext, decryption_key)
    print("DEcrypted: ", decrypted_text)
    return decrypted_text'''

#decrypted_text = Decrypt()
def encrypt():

        # To decrypt, simply XOR the encrypted text with the same key
        encrypted_text = xor_encrypt(decrypted_text, decryption_key)
        print("Encrypted: ", encrypted_text)


