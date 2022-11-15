#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Module 3 Assignment
#Problem 2


# if number 
# return True 
# else
# return False

def is_number(astring):
    valid_number = True
    try:
        #if number of numerical expression, then will convert to float
        float(astring)
    except:
        #if not a number of numerical expression, return false
        valid_number = False
        print("This is not a valid number")
    finally:
        return valid_number

input_string = input("Please enter a number ")

print(is_number(input_string))