#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Module 3 Assignment
#Problem 1

#ask for input temperature
str_temperature_input = input("Enter a temperature in Fahrenheit: ")
valid_temperature_input = True
#try to evaluate string to catch all forms of numerical expressions
try:
    float_temperature_input = eval(str_temperature_input)
except:
    #an exception is raised (not valid input)
    print("Not a valid input")
else:
    #if no exception was raised
    celcius_temperature = (float_temperature_input - 32) * 5/9 
    print(f"The temperature is {celcius_temperature} in Celsius.")


