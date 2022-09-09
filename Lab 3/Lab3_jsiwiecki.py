# Author: Joseph Siwiecki
# Assignment: Lab 3
# Completed: 9/9/2022
# Class: CS 2520.01

# --------------------- TASK 1 ---------------------

# get input, don't convert to float/int because you could also enter a string
a = input("Enter the first value: ")
b = input("Enter the second value: ")
c = input("Enter the third value: ")

# a is the largest
if (a > b and a > c):
    print(a)
    
# b is the largest
elif (b > a and b > c):
    print(b)
    
# c is the largest
else:
    print(c)
    
# OUTPUT:

# TEST 1: 

# Enter the first value: hello
# Enter the second value: how're you
# Enter the third value: hoho
# how're you

# TEST 2:

# Enter the first value: 35.8
# Enter the second value: 28
# Enter the third value: -36.5
# 35.8

# TEST 3:

# Enter the first value: 100
# Enter the second value: hello
# Enter the third value: -50
# hello

# --------------------- TASK 2 ---------------------

count = int(input("Please enter the number of items purchased: "))
total = int(input("Please enter the total cost: "))
print("Average =",  0 if count == 0 else total / count) # if count is 0, average is 0, else calculate average

# OUTPUT:

# TEST 1:

# Please enter the number of items purchased: 0
# Please enter the total cost: 5
# Average = 0

# TEST 2: 

# Please enter the number of items purchased: 5
# Please enter the total cost: 10
# Average = 2.0

# --------------------- TASK 3 ---------------------

# (A)

i = 1
while i < 10:
    i = i + 2
    if i == 5:
        continue
    print(i, end = " ")

# GUESS: 
# For this code segment, I'm going to guess that it will output:
#   3 7 9 11
    
# ACTUAL OUTPUT: 
#   3 7 9 11

# CONCLUSION: 
# My guess is the same, because i is the iterator and we are changing i as expected.

# (B)

for j in range (20):
    j = j + 2
    print(j, end = " ")
    if j == 10:
        break
    
# GUESS: 
# For this code segment, I'm going to guess that it will output:
#   2 3 4 5 6 7 8 9 10 11 12

# ACTUAL OUTPUT: 
#   2 3 4 5 6 7 8 9 10 

# CONCLUSION:
# My guess was incorrect. During our class session on 9/8 you explained that in for loops,
# we can't exactly change the iterator's value in the way it's done in this code segment, so I 
# almost got it correct, but I can't understand why I thought it would print to 12. I think I
# perhaps assumed it would count to 10 and then print 12 but instead when it reached 8, I believe j was technically
# 10 because of the j = j + 2, so it broke out earlier than I thought it would.

# --------------------- TASK 4 ---------------------

sum = 0
num = int(input("Enter a number to check if it is prime: "))
x, count = 2, 0

while (x <= num / 2):
    if (num % x == 0):
        count += 1
        break
    x += 1

if count == 0:
    print(num, "is prime!")

else:
    print(num, "is not prime!")
    

# OUTPUT: 

# TEST 1:
# Enter a number to check if it is prime: 37
# 37 is prime! 

# TEST 2:
# Enter a number to check if it is prime: 35
# 35 is not prime!                          
