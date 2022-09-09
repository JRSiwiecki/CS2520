# Author: Joseph Siwiecki
# Assignment: Lab 2
# Completed: 9/7/2022
# Class: CS 2520.01

# --------------------- TASK 1 ---------------------
# ---------- PROBLEM 1 ----------

# get ages
age1 = int(input("Enter age #1: "))
age2 = int(input("Enter age #2: "))
age3 = int(input("Enter age #3: "))

# calculate averages
average_age_int = (age1 + age2 + age3) // 3
average_age_float = round((age1 + age2 + age3) / 3, 1)

# print to console
print("Average age as an integer: ", average_age_int)
print("Average age as a float: ", average_age_float)

# OUTPUT:

# Enter age #1: 18
# Enter age #2: 22
# Enter age #3: 19
# Average age as an integer:  19
# Average age as a float:  19.7


# ---------- PROBLEM 2 ----------

# get inputs
present_value = int(input("Enter the present value: "))
interest_rate = int(input("Enter the interest rate: "))
years = int(input("Enter the number of years: "))

# calculate and print future value
future_value = present_value * ( 1 + (interest_rate / 100)) ** years
print("Future Value: ", future_value)

# OUTPUT: 

# Enter the present value: 1000
# Enter the interest rate: 5
# Enter the number of years: 30
# Future Value:  4321.942375150667

# ---------- PROBLEM 3 ----------

# get inputs
s1 = input("Enter the 1st string: ")
s2 = input("Enter the 2nd string: ")

# check condition, if true, swap strings
if (s1 > s2):
    s1, s2 = s2, s1

# output strings
print("S1 + S2: " + s1 + s2)
print("S1 * 3: " + s1 * 3)

# OUTPUT: 

# Enter the 1st string: Hi
# Enter the 2nd string: bye
# S1 + S2: Hibye
# S1 * 3: HiHiHi

# Enter the 1st string: Python
# Enter the 2nd string: Java
# S1 + S2: JavaPython
# S1 * 3: JavaJavaJava

# ---------- PROBLEM 4 ----------

# initialize varialbes, use shorthand operators, then output
total = 10
count = 5
count -= 2
total += count
print("Total:", total)
print("Count:", count)

# OUTPUT: 

# Total: 13
# Count: 3 

# ---------- PROBLEM 5 ----------

# get input strings and slice them
input_string = input("Enter a string: ")
substring1 = input_string[7:13]
substring2 = input_string[15:19]

print("Substring 1:", substring1)
print("Substring 2:", substring2)

# OUTPUT: 

# Enter a string: I love Python, hoho
# Substring 1: Python
# Substring 2: hoho

# Enter a string: Try learning Rust, maybe?
# Substring 1: rning
# Substring 2: st,

# --------------------- TASK 2 ---------------------

# Get user inputs
# Age and salary are casted to integers
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
company = input("Enter the company you wish to work: ")
salary = int(input("Enter your monthly salary: "))

# calculate monthly salary then cast to string to print it easily
salary *= 12
salary = str(salary)

# print output
print("My name is " + name + ", my age is", age)
print("I hope to work for", company, "and earn $" + salary + " a year.")

# OUTPUT: 

# Please enter your name: Alice Wonderland
# Please enter your age: 20
# Enter the company you wish to work: Google
# Enter your monthly salary: 8000
# My name is Alice Wonderland, my age is 20
# I hope to work for Google and earn $96000 a year.

# Please enter your name: Joseph Siwiecki
# Please enter your age: 20
# Enter the company you wish to work: Riot Games
# Enter your monthly salary: 10000
# My name is Joseph Siwiecki, my age is 20
# I hope to work for Riot Games and earn $120000 a year.


