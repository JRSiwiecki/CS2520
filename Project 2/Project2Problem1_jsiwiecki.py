# Author: Joseph Siwiecki
# Assignment: Project 2 Problem 1
# Completed: 10/10/2022
# Class: CS 2520.01

import hashlib

# --------------------- PROBLEM 1 ---------------------

# ----------- PART 1 -----------
def get_num_of_characters(str):
    return len(str)

# ----------- PART 2 -----------
def output_without_whitespace(str):
    temp = str.replace(" ", "")
    output = temp.replace("\t", "")
    return output

# ----------- PART 3 -----------
def get_acronym(str):
    acronym = ""
    words = str.split()
    for word in words:
        acronym += word[0]
    return acronym.upper()

# ----------- PART 4 -----------
def get_safe(str):
    return hashlib.sha256(str.encode("utf-8")).hexdigest()

# ----------- PART 5 -----------
def main():
    # TEST CASE 1
    user_string_1 = input("Enter a sentence or phrase: ")
    print("You entered:", user_string_1)
    print("Number of characters:", get_num_of_characters(user_string_1))
    print("String with no whitespace:", output_without_whitespace(user_string_1))

    user_string_2 = input("Enter a phrase to generate an acronym: ")
    acronym = get_acronym(user_string_2)
    print("The acronym is:", acronym)
    print("Encrypting", acronym, "using SHA 256:", get_safe(acronym))
    
    # TEST CASE 2
    user_string_3 = input("Enter a sentence or phrase: ")
    print("You entered:", user_string_3)
    print("Number of characters:", get_num_of_characters(user_string_3))
    print("String with no whitespace:", output_without_whitespace(user_string_3))

    user_string_4 = input("Enter a phrase to generate an acronym: ")
    acronym = get_acronym(user_string_4)
    print("The acronym is:", acronym)
    print("Encrypting", acronym, "using SHA 256:", get_safe(acronym))
    
    # TEST CASE 3
    user_string_5 = input("Enter a sentence or phrase: ")
    print("You entered:", user_string_5)
    print("Number of characters:", get_num_of_characters(user_string_5))
    print("String with no whitespace:", output_without_whitespace(user_string_5))

    user_string_6 = input("Enter a phrase to generate an acronym: ")
    acronym = get_acronym(user_string_6)
    print("The acronym is:", acronym)
    print("Encrypting", acronym, "using SHA 256:", get_safe(acronym))

# ----------- PART 6 -----------
main()

# OUTPUT

# TEST CASE 1
# Enter a sentence or phrase: The only thing we have to fear is fear itself.
# You entered: The only thing we have to fear is fear itself.     
# Number of characters: 46
# String with no whitespace: Theonlythingwehavetofearisfearitself.
# Enter a phrase to generate an acronym: random access memory
# The acronym is: RAM
# Encrypting RAM using SHA 256: bf4b0c03c646add9b518fc4f658deba189e5bc4918607186e4570472bf6cb19f

# TEST CASE 2
# Enter a sentence or phrase: Yo Mr. White!
# You entered: Yo Mr. White!
# Number of characters: 13
# String with no whitespace: YoMr.White! 
# Enter a phrase to generate an acronym: League of Legends
# The acronym is: LOL
# Encrypting LOL using SHA 256: 6e0290d62f6db1779d6318df50209de8c9b93adb29b7dd46e7b563f044103b40

# TEST CASE 3
# Enter a sentence or phrase: let's get funky :)
# You entered: let's get funky :)
# Number of characters: 18
# String with no whitespace: let'sgetfunky:)
# Enter a phrase to generate an acronym: Young Men's Christian Association
# The acronym is: YMCA
# Encrypting YMCA using SHA 256: 9eba66476e56d37c130818e9932de9d35f2b491ce8e3231897c2c07ae76f5e01
        