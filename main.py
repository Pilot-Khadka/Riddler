# Riddle an alternate version of Cesar Cipher
# Currently only supports Encrypting and Lower case characters

SHIFT = 3  # The shift variable for encryption
# function to convert input data to ascii


def text_to_ascii(data):
    data_ascii = list()  # stores the ascii value of all the input char
    for char in data:
        index = ord(char)
        data_ascii.append(index)
    return data_ascii

def remove_space(data):
    spaces = [pos for pos, char in enumerate(data) if char == " "]
    data.replace(" ","")
    return data,spaces
    
def add_space(data,spaces):
    for space in spaces:
        data = data[:space] + ' ' + data[space:]
    return data
    
    
# encrypting fuction
def encrypt(data):
    data,space = remove_space(data)
    
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
                
    add_space(cipher,space)
    return cipher


if __name__ == '__main__':
    usr_data = input("Enter the text to Encrypt:")
    encrypted = encrypt(usr_data)
    print(encrypted)
