#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Module 3 Assignment
#Problem 3

#encryption function
def caesar_encrypt(key, message):
    #start with empty string
    encrypted_message = ""
    """Encrypt a message by shifting all letters by key"""
    #iterate every character including spaces and punctation to retain all structure excld. letters
    for index in range(0,len(message)):
        #Check if the character is an uppercase or lowercase letter
        if message[index].isupper():
            #append shifted character to encrypted message
            encrypted_message += chr((ord(message[index]) + key - 65) % 26 + 65)
        elif message[index].islower():
            #append shifted character to encrypted message
            encrypted_message += chr((ord(message[index]) + key - 97) % 26 + 97)
        elif message[index].isnumeric():
            encrypted_message += chr((ord(message[index]) + key - 48) % 10 + 48)
        else:
        #if not a letter, do nothing
            encrypted_message += message[index]
    return encrypted_message

#decryption function
def caesar_decrypt(key, message):
    #start with empty string
    decrypted_message = ""
    """Encrypt a message by shifting all letters by key"""
    #iterate every character including spaces and punctation to retain all structure excld. letters
    for index in range(0,len(message)):
        #Check if the character is an uppercase or lowercase letter
        if message[index].isupper():
            #append shifted character to decrypted message
            decrypted_message += chr((ord(message[index]) - key - 65) % 26 + 65)
        elif message[index].islower():
            #append shifted character to decrypted message
            decrypted_message += chr((ord(message[index]) - key - 97) % 26 + 97)
        #if a number
        elif message[index].isnumeric():
            decrypted_message += chr((ord(message[index]) - key - 48) % 10 + 48)
        else:
        #if not a letter, do nothing
            decrypted_message += message[index]
    return decrypted_message

input_message = "Experience is the teacher of all things."
example_encrypted_message = caesar_encrypt(12, input_message)
print(example_encrypted_message)

example_decrypted_message = caesar_decrypt(12, example_encrypted_message)
print(example_decrypted_message)
