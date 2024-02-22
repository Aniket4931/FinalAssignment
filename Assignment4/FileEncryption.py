import string
"""
Assignment 4: File Encryption
Create a Python script that encrypts and decrypts text files using a simple substitution cipher. 
Implement functions for encryption and decryption using a basic substitution cipher algorithm (e.g., shifting each letter by a fixed number of positions in the alphabet).
Prompt users to enter a filename and choose whether to encrypt or decrypt the file.
Ensure the script handles cases where the file does not exist or cannot be opened for reading/writing.
"""

a=open("C:/Users/ADMIN/OneDrive/Documents/FinalAssignment/Assignment4/a.txt","r")
text=a.read()
shift = 4

def Encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypts(text, shift):
    return Encrypt(text, -shift)

encrypted_text = Encrypt(text, shift)
print("Encrypted text:")
print(encrypted_text,"\n")

decrypted_text = decrypts(encrypted_text, shift)
print("Decrypted text:")
print(decrypted_text)
