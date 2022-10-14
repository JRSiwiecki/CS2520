# Author: Joseph Siwiecki
# Assignment: Lab 6
# Completed: 10/13/2022
# Class: CS 2520.01

# --------------------- TASK 1 ---------------------
# ---------- PART 1 ----------
# print("Enter three strings: ")
# string_one = input("1st String: ")
# string_two = input("2nd String: ")
# string_three = input("3rd String: ")

# # ---------- PART 2 ----------
# character_one = max(string_one)
# character_two = max(string_two)
# character_three = max(string_three)

# print("Largest character in the 1st string:", character_one)
# print("Largest character in the 2nd string:", character_two)
# print("Largest character in the 3rd string:", character_three)

# largest_string = max(string_one, string_two, string_three)
# print("The largest of the three strings:", largest_string)


# # ---------- PART 3 ----------
# special_character = input("Enter the special character or string you want in between the strings: ")
# special_string = string_one + special_character + string_two + special_character + string_three
# print("Special string:", special_string)

# OUTPUT

# TEST CASE 1
# Enter three strings: 
# 1st String: Hello
# 2nd String: You
# 3rd String: Bye
# Largest character in the 1st string: o
# Largest character in the 2nd string: u
# Largest character in the 3rd string: y
# The largest of the three strings: You
# Enter the special character or string you want in between the strings: #
# Special string: Hello#You#Bye

# TEST CASE 2
# Enter three strings: 
# 1st String: Cloud 9
# 2nd String: Fnatic
# 3rd String: Edward Gaming
# Largest character in the 1st string: u
# Largest character in the 2nd string: t
# Largest character in the 3rd string: w
# The largest of the three strings: Fnatic
# Enter the special character or string you want in between the strings: L
# Special string: Cloud 9LFnaticLEdward Gaming

# --------------------- TASK 2 ---------------------
# ---------- PART 1 ----------
L1 = []

while True:
    num = input("Enter a float or enter Q to quit: ")
    
    if num == "Q" or num == "q":
        break
    
    else:
        num = float(num)
        L1.append(num)

print("List 1:", L1)

# ---------- PART 2 ----------
import random
num_of_floats = int(input("Enter the amount of floats you would like to generate: "))

L2 = [random.uniform(0.0, 10.0) for i in range(num_of_floats)]

print("List 2: ", L2)

# ---------- PART 3 & 4 ----------
if len(L1) < len(L2):
    L2.extend(L1)
    print("List 2 with List 1: ", L2)
    print("Last element of List 2:", L2.pop())
    L2.reverse()
    print("List 2 reversed:", L2)
else:
    L1.extend(L2)
    print("List 1 with List 2:", L1)
    print("Last element of List 1:", L1.pop())
    L1.reverse()
    print("List 1 reversed:", L1)

# OUTPUT

# TEST CASE 1
# Enter a float or enter Q to quit: 10.2
# Enter a float or enter Q to quit: 20.1
# Enter a float or enter Q to quit: 15.2
# Enter a float or enter Q to quit: q
# List 1: [10.2, 20.1, 15.2]
# Enter the amount of floats you would like to generate: 5
# List 2:  [7.122717875130915, 0.3431109409383093, 5.9142531760824895, 3.927691627893224, 2.8806109838216165]
# List 2 with List 1:  [7.122717875130915, 0.3431109409383093, 5.9142531760824895, 3.927691627893224, 2.8806109838216165, 10.2, 20.1, 15.2]
# Last element of List 2: 15.2
# List 2 reversed: [20.1, 10.2, 2.8806109838216165, 3.927691627893224, 5.9142531760824895, 0.3431109409383093, 7.122717875130915]

# TEST CASE 2
# Enter a float or enter Q to quit: 992.1
# Enter a float or enter Q to quit: 5324.2
# Enter a float or enter Q to quit: 0.2
# Enter a float or enter Q to quit: 1.2224
# Enter a float or enter Q to quit: 86943.2
# Enter a float or enter Q to quit: 58301.2
# Enter a float or enter Q to quit: 3463.2
# Enter a float or enter Q to quit: 22.346534
# Enter a float or enter Q to quit: 123.1
# Enter a float or enter Q to quit: q
# List 1: [992.1, 5324.2, 0.2, 1.2224, 86943.2, 58301.2, 3463.2, 22.346534, 123.1]
# Enter the amount of floats you would like to generate: 9
# List 2:  [2.033252105436852, 1.9237858547902897, 7.189870625773569, 1.8021226829820602, 5.072030485009749, 
# 3.3274370225736085, 5.335625938058795, 4.556324909928574, 2.4832958245060253]
# List 1 with List 2: [992.1, 5324.2, 0.2, 1.2224, 86943.2, 58301.2, 3463.2, 22.346534, 123.1, 2.033252105436852, 1.9237858547902897, 7.189870625773569, 1.8021226829820602, 
# 5.072030485009749, 3.3274370225736085, 5.335625938058795, 4.556324909928574, 2.4832958245060253]
# Last element of List 1: 2.4832958245060253
# List 1 reversed: [4.556324909928574, 5.335625938058795, 3.3274370225736085, 5.072030485009749, 1.8021226829820602, 7.189870625773569, 1.9237858547902897, 2.033252105436852, 
# 123.1, 22.346534, 3463.2, 58301.2, 86943.2, 1.2224, 0.2, 5324.2, 992.1]

# --------------------- TASK 3 ---------------------
# ---------- PART 1 ----------