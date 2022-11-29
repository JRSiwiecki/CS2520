# Author: Joseph Siwiecki
# Assignment: Lab 10
# Completed: 11/28/2022
# Class: CS 2520.01

from math import sqrt

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
def gen_sort(cmp, lst):
    
    return sorted(lst, key=cmp)

def is_bigger(x, y):
    if x > y:
        return True
    
    else:
        return False
    
def alphabetical_order(x,  y):
    if len(x) == len(y) and x < y:
        return True
    
    else:
        return False

def bigger_name_or_count(x, y):
    if x[0] == y[0]:
        if x[1] > y[1]:
            return True
        else:
            return False
    
    elif x[0] > y[0]:
        return True
    
    else:
        return False
    
    
def task_2_tests():
    print(gen_sort(is_bigger, [5, 2, 12, 4, 9, 13, 22, 1, 6, 17]))


# --------------------- TASK 3 ---------------------
def double_list(lst):
    doubled = list(map(lambda x: x * 2, lst))
    return doubled

def squared_list(lst):
    odds = list(filter(lambda x: x % 2 != 0, lst))
    squared = list(map(lambda x: x * x, odds))
    return squared

def primes_list(lst):
    primes = list(filter(is_prime, lst))
    return primes
    
def is_prime(n):
    if n <= 1:
        return False
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True

def task_3_tests():
    l1 = [x for x in range(1, 100)]
    print(l1)
    
    print("Doubled List:", double_list(l1))
    print("Squared List:", squared_list(l1))
    print("Primes List:", primes_list(l1))
        
def main():
    # task_1_tests()
    task_2_tests()
    # task_3_tests()

main()