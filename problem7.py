#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Module 3 Assignment
#Problem 7

#example

def centered_average_with_iteration(numbers): 
    """Approach 1 - Using iteration"""

    #cleaning of input list
    try:
        input_list = numbers.split(',')
        input_list = [int(number) for number in input_list]
        input_list.sort()
    except:
        print("not valid input")

    try:
        len(input_list)>=3
    except:
        print("there are less than 3 items in the list")
    else:
        #find out min and maxes
        min_of_numbers = input_list[0]
        for number in input_list:
            if min_of_numbers > number:
                min_of_numbers = number

        max_of_numbers = input_list[0]
        for number in input_list:
            if max_of_numbers < number:
                max_of_numbers = number
    

    #remove duplicate copies of max and min
    while input_list.count(min_of_numbers)>1:
        input_list.remove(min_of_numbers)
    while input_list.count(max_of_numbers)>1:
        input_list.remove(max_of_numbers)

    #initiate center sum
    center_sum = 0

    #iterate over list items
    for index in range(1,len(input_list)-1):
        center_sum += input_list[index]

    #calculate average
    average = center_sum / (len(input_list)-2)

    return average 


def centered_average(numbers): 
    """Approach 2 - No iteration allowed"""

    #cleaning of input list   
    try:
        input_list = numbers.split(',')
        input_list = [int(number) for number in input_list]
        input_list.sort()
    except:
        print("not valid input")

    try:
        len(input_list)>=3
    except:
        print("there are less than 3 items in the list")
    else:
        #find out min and max
        min_of_numbers = min(input_list)
        max_of_numbers = max(input_list)
   
    #find location of last min and first max
    #find last location of min, by reversing and finding first location, this is a reverse index starting from the end
    input_list.reverse()
    start_index_from_end = input_list.index(min_of_numbers)

    #flip list back to normal
    input_list.reverse()
    #find first instance of max
    stop_index = input_list.index(max_of_numbers)

    #remove duplicate head and tails
    new_list = input_list[len(input_list)-start_index_from_end:stop_index]
    average = sum(new_list)/(len(new_list))
    
    return average

