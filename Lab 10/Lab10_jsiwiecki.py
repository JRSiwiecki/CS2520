# Author: Joseph Siwiecki
# Assignment: Lab 10
# Completed: 11/28/2022
# Class: CS 2520.01

# --------------------- TASK 1 ---------------------
def is_palindrome(s):
    # remove non alphanumeric characters 
    # (leave only characters in alphabet)
    s = ''.join(filter(str.isalnum, s))
    
    # ignore cases, so lowercase letters only
    s = s.lower()
    
    # base case
    # a 1 character string is a palindrome
    if len(s) <= 1:
        return True
    
    # if the current 1st character and current last character are equal
    # then call recursively with the 1st and last character sliced
    elif s[0] == s[-1]:
        return is_palindrome(s[1:len(s) - 1])
    
    # if the current 1st character and current last character are NOT equal
    # then the string can't be a palindrome
    else:
        return False

def task_1_tests():
    print("\"never odd or even\" is a palindrome?:", is_palindrome("never odd or even"))
    print("\"no lemon, no melon\" is a palindrome?:", is_palindrome("no lemon, no melon"))
    print("\"A Man, A Plan, A Canal – Panama!\" is a palindrome?:", is_palindrome("A Man, A Plan, A Canal – Panama!"))
    print("\"i ain't afraid of no ghosts\" is a palindrome?:", is_palindrome("i ain't afraid of no ghosts"))

# --------------------- TASK 2 ---------------------
    
def main():
    task_1_tests()

main()