#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Module 3 Assignment
#Problem 4


def process_file(filename): 
    """Read, sort and return a file""" 

    #initiate empty list
    sorted_items = []
    
    #open file
    try:
        file_handle = open(filename, 'r')
    except:
        print("error reading file")
    else:
        #iterate over file lines
        for line in file_handle:
            clean_line = line.strip()
        #sort the items in the line    
            sorted_items.append(clean_line)
    
    #check what is in sorted_items 
    sorted_items.sort()
    number_of_lines = len(sorted_items)

    file_handle.close()

    # Return a tuple
    return filename, sorted_items, number_of_lines

# Snippet to run function
(filename, items, lines) = process_file("common_words.txt")
