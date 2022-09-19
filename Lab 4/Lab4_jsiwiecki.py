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

# I predict that this code will have an error, because firstly, there is no
# function defined as prob1, we only have a prob2 function.
# Secondly, even if the first print statement had no errors, we are attempting
# to print i outside of the scope of the variable. i was declared within the function boundaries
# and thus is only accessible from within the function's scope. Because we are trying to access
# i outside of the function, an error will occur.

def prob2(): 
    for i in range(4):
        print(i, end = " ")

print(prob1())
print("i = ", i)

# EXPLANATION: 

# My prediction was mostly correct, as the first print statement outside of the function throws an error,
# and the second one doesn't run because the program crashed. If the second one did run, it would also throw an error.

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

# --------------------- TASK 3 ---------------------