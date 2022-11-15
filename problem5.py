#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Module 3 Assignment
#Problem 5

#import encryption/decryption functions from problem 3 file
from problem3 import caesar_encrypt
from problem3 import caesar_decrypt

#import function to process the common text file
from problem4 import process_file

#given message
given_message = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"
given_message_split = given_message.split()

#generate the list of most common words sorted
(filename, common_words, lines) = process_file("common_words.txt")

#attempt to decrypt the words
decryption_key = 0
#try keys
for key in range(1,26):
    decrypted_message = []
    for word in given_message_split:
        decrypted_message.append(caesar_decrypt(key,word))
    for decrypted_word in decrypted_message:
        if decrypted_word in common_words:
            decryption_key = key

print(f"The decryption key is {decryption_key}, and the message is {caesar_decrypt(decryption_key,given_message)}" )

# the caesar encryption key is 15 spaces and the decrypted message is ("believe you can and you are halfway there")