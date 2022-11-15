#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Module 3 Assignment
#Problem 9

#to get all punctuation

#import function to process the common text file
from problem4 import process_file

#get common words
(filename, common_words, lines) = process_file("common_words.txt")

#process speech file
try:
    file_handle = open("speech.txt", 'r')
    clean_lines = []
except:
    print("error reading file")
else:
    #iterate over file lines
    for line in file_handle:
        #clean lines of whitespaces and punctuation
        clean_line = line.strip()
        #add to split_lines
        clean_lines.append(clean_line)

    file_handle.close()

#single string speech
single_string_speech = ""
for line in clean_lines:
    single_string_speech += line

#find all punctuation
punctuations = []
for character in single_string_speech:
    if character.isalpha():
        pass
    else:
        punctuations.append(character)

#find all unique punctuation
unique_punctuations = list(set(punctuations))
#exclude white spaces
unique_punctuations.remove(' ')

#remove all punctuation from single string speech
for punctuation in unique_punctuations:
    single_string_speech = single_string_speech.replace(punctuation,' ')

#turn all letters lower case
all_MLK_words = single_string_speech.lower()

#get a list of all MLK words 
all_MLK_words = all_MLK_words.split()

#create a set of unique MLK words
unique_MLK_words = list(set(all_MLK_words))

#create a set of unique MLK words that are not in common_words.txt
#remove single letter words from apostrophes 's, 't, etc.
non_common_unique_MLK_words = [word for word in unique_MLK_words if len(word)>1 and word not in common_words]

#sort unique MLK words that are uncommon
non_common_unique_MLK_words.sort()

#create dictionary of most common words used by MLK
MLK_freq_words = {}

#assinging counts of words to each word in the speech
for word in non_common_unique_MLK_words:
    MLK_freq_words[word] = all_MLK_words.count(word)

#using a list to get the key, value paris in tuples to be able to sort
MLK_freq_list = []
for key in MLK_freq_words:
    MLK_freq_list.append((key,MLK_freq_words[key]))

#sorting by the counts of the words
sorted_MLK_freq_words = dict(sorted(MLK_freq_words.items(), key = lambda item: item[1], reverse = True))

#taking the top 25 
top_25_MLK = list(sorted_MLK_freq_words.items())[:25]

#wrtie the top 25 results into a txt file 
try:
    file_handle = open('sorted_MLK_Top25_words.txt','w')
except:
    print("could not write file")
else:
    for pair in top_25_MLK:
        file_handle.write(f"{pair[0]} - {pair[1]}\n")




