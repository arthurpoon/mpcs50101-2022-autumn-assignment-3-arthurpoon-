#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Module 3 Assignment
#Problem 8

#Get input from bases.txt
#open file

try:
    file_handle = open("bases.txt", 'r')
    split_lines = []
except:
    print("error reading file")
else:
    #iterate over file lines
    for line in file_handle:
        #clean lines of whitespaces
        clean_line = line.strip()
        split_line = clean_line.split()
        #add to split_lines
        split_lines.append(split_line)

#merge content of split_lines into a single string

bases_single_sequence = ""

for line in split_lines:
    bases_single_sequence += line[0]

#calculate distribution, rounding to nearest integer, and storing result as integer
total_length = len(bases_single_sequence)
A_percentage = int(round(bases_single_sequence.count("A")/total_length * 100 , 0))
T_percentage = int(round(bases_single_sequence.count("T")/total_length * 100 , 0))
C_percentage = int(round(bases_single_sequence.count("C")/total_length * 100 , 0))
G_percentage = int(round(bases_single_sequence.count("G")/total_length * 100 , 0))

#printing out results
print(f"A: {A_percentage}%")
print(f"T: {T_percentage}%")
print(f"C: {C_percentage}%")
print(f"G: {G_percentage}%")
