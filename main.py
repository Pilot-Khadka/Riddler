# Riddle an alternate version of Cesar Cipher
# Currently only supports Encrypting

import pyfiglet

SHIFT = 4  # The shift variable for encryption
# function to convert input data to ascii


def text_to_ascii(data):
    data_ascii = list()  # stores the ascii value of all the input char
    for char in data:
        index = ord(char)
        data_ascii.append(index)
    return data_ascii


# encrypting fuction
def encrypt(data):
    text = text_to_ascii(data)
    temp = 0
    cipher = ''
    for letter in text:
        if letter in range(128):
            if letter == 32:
                cipher += chr(letter)
            elif letter < 64:
                index = letter - ord('0')
                temp = (index + SHIFT) % 10
                cipher += chr(temp + ord('0'))
            elif letter < 97:
                index = letter - ord('A')
                temp = (index + SHIFT) % 26
                cipher += chr(temp + ord('A'))
            else:
                index = letter - ord('a')
                temp = (index + SHIFT) % 26
                cipher += chr(temp + ord('a'))

    return cipher


# Decryption will decrypt the given text by finding most common letter
# ETA are most repeated letters in English

def decrypt(data):
    rep_1 = ''
    rep_2 = ''
    rep_3 = ''
    data.lower()
    size = len(data)
    data_ascii = text_to_ascii(data)
    data_dict = dict()
    data_list = list()  # list of Tuple storing letter and times of repeat
    for letter in data_ascii:
        if letter != 32:
            data_dict[letter] = data_dict.get(letter, 0)+1

    # Changing to Tuple (no_of_repetition, char )
    for k, v in data_dict.items():
        data_list.append((v, k))

    # A tuple of sorted char with no of repetitions
    data_sorted = sorted(data_list, reverse=True)

    # The most repeated char in ASCII
    first = data_sorted[0][1]
    sec = data_sorted[1][1]
    third = data_sorted[2][1]

   # Finding the shift , E is supposed to be most repeated character
    shift = first-ord('e')
    if (sec-ord('t') == shift and third-ord('a') == shift):
        # shift sucessfuly found
        plain = decrypter(shift, data)
    else:
        plain = "CANNOT DECRYPT!"

    return plain

# Decrypts the text using shift from decrypt()


def decrypter(shift, data):
    text = text_to_ascii(data)
    temp = 0
    plain = ''
    for letter in text:
        if letter in range(128):
            if letter == 32:
                plain += chr(letter)
            elif letter < 64:
                index = letter - ord('0')
                temp = (index - SHIFT) % 10
                plain += chr(temp + ord('0'))
            elif letter < 97:
                index = letter - ord('A')
                temp = (index - SHIFT) % 26
                plain += chr(temp + ord('A'))
            else:
                index = letter - ord('a')
                temp = (index - SHIFT) % 26
                plain += chr(temp + ord('a'))

    return plain


if __name__ == '__main__':

    intro = pyfiglet.figlet_format("RIDDLER")
    print(intro,end="")

    print("""
[1]. Encrypt
[2]. Decrypt""")
    option = int(input("Select an Option:"))

    if option == 1:
        usr_data = input("Enter the text to Encrypt:")
        encrypted = encrypt(usr_data)
        print(encrypted)
    elif option == 2:
        # data input for decrypt
        cipher = input("Enter the Data:")
        print(decrypt(cipher))
    else:
        print("Invalid Input")
