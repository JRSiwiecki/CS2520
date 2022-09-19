# Author: Joseph Siwiecki
# Assignment: Project 1
# Completed: 9/13/2022
# Class: CS 2520.01

from math import pi
from math import factorial
from math import sin

# --------------------- TASK 1 ---------------------

# get the user's choice of calculator, make sure it is either "USA" or "Metric"
# if it isn't, keep asking
while True:
    choice = input("Enter USA to use the Imperial Calculator or Metric to use the Metric Calculator: ")
    
    # nested loop here to see if the value entered is a 0 or 1, if not, then ask for input again
    if choice == "USA" or choice == "Metric":
        break
        
    else:
        continue

# use two separate while loops to get height and weight.
# use try/except to make sure that user enters an int/float and not a string
# user will enter their inputs in their units of choice.
# for both inputs, ensure that the input is not less than 0, because otherwise the bmi would either be undefined or 0 or negative, 
# which cannot be possible!
while True:
    weight = input("Please enter your weight: ")
    
    try:
        weight = float(weight)
        
        if weight <= 0:
            continue
        else:
            break
    except ValueError:
        continue
    
    
# similar to height while loop, but just getting weight in the same manner.
# user will enter their inputs in their units of choice.
while True:
    height = input("Please enter your height: ")
    
    try:
        height = float(height)
        
        if height <= 0:
            continue
        else:
            break
        
    except ValueError:
        continue
        

    
# use usa or metric calculator based on user input
if choice == "USA":
    bmi = 703 * (weight / (height * height))
    print("USA: ", bmi)

else:
    bmi = (weight / (height * height))
    print("Metric: ", bmi)
    
if bmi >= 18 and bmi <= 25:
    print("You have a normal BMI.")
    
elif bmi < 18:
    print("You have an underweight BMI.")
    
else:
    print("You have an overweight BMI.")
    
    
# --------------------- TASK 2 ---------------------

# infinite loop, user exits when they please
while True:
    
    # get input and evaluate it with the math library in case "pi" is entered
    value = input("Enter an x value in radians (x must be in the range [-π, π]), or enter Q to quit: ")
    
    # sentinel value
    if value == "Q" or value == "q":
        break
    
    # separate value to print original input later
    x = value
    
    # use try except in case the user enters an invalid input (not a number)
    try:
        x = eval(value)
    
    except: 
        print("Your input is invalid!")
    
    # check if input is out of range
    if x < -pi or x > pi:
        print("Your input is out of range!")
        continue
    
    # keep track of result and count (for number of loop iterations)
    result = 0
    count = 0
    
    for i in range(0, 150):
        
        # taylor series formula
        result += ( ( -1 ) ** i ) / ( factorial ( ( 2 * i ) + 1 ) ) * ( x ** ( ( 2 * i ) + 1 ) )
        
        # increment count
        count += 1
        
        # print intermediate result
        print("Iteration", count, "=", result)
        
        # keep track of absolute difference between my calculation and python's sin function
        difference = abs(result - sin(x))
        
        # if the difference between my result and python's result is low enough, stop calculations
        if difference < 0.000001:
            break
        
    # round result after calculation for more consistent comparison experience
    result = round(result, 8)
    print("When x =", value, "--> sin(x) using Taylor's formula is", result, "~", count, "loops")
