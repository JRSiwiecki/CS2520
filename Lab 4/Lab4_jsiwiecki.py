# Author: Joseph Siwiecki
# Assignment: Lab 4
# Completed: 9/19/2022
# Class: CS 2520.01

from math import fsum

# --------------------- TASK 1 ---------------------

normal_sum = sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
f_sum = fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])

print("Normal sum:", normal_sum)
print("fsum:", f_sum)

# OUTPUT: 

# Normal sum: 0.9999999999999999
# fsum: 1.0

# EXPLANATION: 

# We are adding .1 exactly 10 times, which to humans, is just 1.0 or 1.
# However, python's built-in sum function likely has challenges being precise 
# with floating point arithmetic, and so even though we know the answer is 1.0,
# python using its built-in sum function can not add correctly and is inprecise/inaccurate
# due to rounding errors that occur in calculations.

# When using the math library's fsum however, it not only adds floats together similar to the 
# normal sum function, but it keeps track of any rounding errors to ensure accuracy, and thus
# we get the expected answer of 1.0 that the normal sum function was unable to produce.

# --------------------- TASK 2 ---------------------

# PREDICTION:

# I predict that this code will print 0 1 2 3 None, and then throw an error, crashing the program.
# The prob2 function doesn't return anything, it just prints 0 1 2 3, so trying to print the function
# will result in None.
# In the second print statement outside of the function, we are attempting to
# to print i outside of the scope of the variable. i was declared within the function boundaries
# and thus is only accessible from within the function's scope. Because we are trying to access
# i outside of the function, an error will occur.

def prob2(): 
    for i in range(4):
        print(i, end = " ")

print(prob2())
# print("i = ", i) # THIS LINE IS COMMENTED OUT SO THE REST OF THE PROGRAM CAN RUN


# OUTPUT (this is the output if the final print statement in task 2 was not commented out): 

# 0 1 2 3 None
# Traceback (most recent call last):
#   File "c:\Users\JRSiw\Desktop\Programming\School Workspace\CS2520\Lab 4\Lab4_jsiwiecki.py", line 49, in <module>
#     print("i = ", i)
# NameError: name 'i' is not defined. Did you mean: 'id'?

# EXPLANATION: 

# My prediction was correct, as the first print statement outside of the function prints None, 
# because our function doesn't return anything,
# and the second one crashes the program because
# we can't access i outside the function.

# --------------------- TASK 3 ---------------------

def fun(x = 1, y = 2):
    x = x + y
    y += 1
    return x * y

a, b = 3, 2

# These 3 function calls pass in constants.
fun_1 = fun(3, 2)
fun_2 = fun(y = 2, x = 3)
fun_3 = fun(x = 3)

# These last 2 function calls pass in other variables.
fun_4 = fun(a, b)
fun_5 = fun(x = a, y = b)

print("fun 1:", fun_1)
print("fun 2:", fun_2)
print("fun 3:", fun_3)
print("fun 4:", fun_4)
print("fun 5:", fun_5)

# OUTPUT: 

# fun 1: 15
# fun 2: 15
# fun 3: 15
# fun 4: 15
# fun 5: 15

# --------------------- TASK 4 ---------------------

def grade_test(test_score):
    
    if test_score > 100:
        return "Invalid score; too high."
    
    elif test_score >= 90: 
        return "A"
    
    elif test_score >= 80:
        return "B"
    
    elif test_score >= 70:
        return "C"
    
    elif test_score >= 60:
        return "D"
    
    elif test_score >= 0:
        return "F"
    
    elif test_score < 0:
        return "Invalid score; too low."
    
while True:
    student_score = input("Enter your test score (or enter Q to quit): ")
    
    if student_score == "q" or student_score == "Q":
        break
    
    student_score = int(student_score)
    student_grade = grade_test(student_score)
    
    print("Your letter grade is:", student_grade)
    
# OUTPUT: 

# Enter your test score (or enter Q to quit): -5
# Your letter grade is: Invalid score; too low.
# Enter your test score (or enter Q to quit): 105
# Your letter grade is: Invalid score; too high.
# Enter your test score (or enter Q to quit): 100
# Your letter grade is: A
# Enter your test score (or enter Q to quit): 87
# Your letter grade is: B
# Enter your test score (or enter Q to quit): 69
# Your letter grade is: D
# Enter your test score (or enter Q to quit): 33
# Your letter grade is: F
# Enter your test score (or enter Q to quit): 77
# Your letter grade is: C
# Enter your test score (or enter Q to quit): q
        