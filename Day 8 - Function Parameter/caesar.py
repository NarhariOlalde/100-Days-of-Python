def encrypt(text, key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            encrypted += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted += char
    return encrypted

def decrypt(text, key):
    decrypted = ""
    for char in text:
        if char.isalpha():
            decrypted += chr((ord(char) - key - 97) % 26 + 97)
        else:
            decrypted += char
    return decrypted

def insert_text():
    menu = int(input("Menu: \n1. Encrypt \n2. Decrypt \n3. Exit \n"))
    if menu == 1:
        text = input("Text: ")
        key = int(input("Key: "))
        print(encrypt(text, key))
    elif menu == 2:
        text = input("Text: ")
        key = int(input("Key: "))
        print(decrypt(text, key))
    elif menu == 3:
        exit()
    else:
        print("Invalid input")
        insert_text()


insert_text()