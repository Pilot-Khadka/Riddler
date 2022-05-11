# Cesar Cipher
# shift = 3
# Currently only supports Encrypting and Lower case characters

plain = 'abcdefghijklmopqrstuvwxyz'

def encrypt(text):
    text = text.lower()
    temp = 0
    cipher = ''
    for letter in text:
        if letter in plain:
            index = ord(letter) - ord('a')
            temp = (index + 3) % 26
            cipher += chr(temp + ord('a'))
    return cipher


print(encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
