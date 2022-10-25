# Author: Joseph Siwiecki
# Assignment: Lab 7
# Completed: 10/24/2022
# Class: CS 2520.01

import random

# --------------------- TASK 1 ---------------------

# get words list
words = []
sentence = input("Enter a sentence: ")
words = sentence.split()
        
# create dictionary with words as keys and frequencies as pairs
words_frequencies = {}

for word in words:
    word_count = words.count(word)
    words_frequencies[word] = word_count

print("Dictionary:", words_frequencies)

# create nested tuple from dict with list comprehension
words_frequencies = [(k, v) for k, v in words_frequencies.items()]

# sort nested tuple by highest occurences in ascending order
for i in range(0, len(words_frequencies)):
    for j in range(0, len(words_frequencies) - i - 1):
        if (words_frequencies[j][1] > words_frequencies[j + 1][1]):
            temp = words_frequencies[j]
            words_frequencies[j] = words_frequencies[j + 1]
            words_frequencies[j + 1] = temp

# print most frequents elements
print("1st Most Frequent Element:", words_frequencies[-1])
print("2nd Most Frequent Element:", words_frequencies[-2])
print("3rd Most Frequent Element:", words_frequencies[-3])

# OUTPUT: 

# TEST CASE 1
# Dictionary: {'python': 4, 'is': 2, 'an': 1, 'easy': 4, 'language': 1, 'to': 3, 'learn': 1, 'and': 1, 'code': 1, 'a': 1, 
# 'lot': 1, 'of': 1, 'modules': 1, 'that': 1, 'are': 1, 'use': 1, 'go': 1}
# 1st Most Frequent Element: ('easy', 4)
# 2nd Most Frequent Element: ('python', 4)
# 3rd Most Frequent Element: ('to', 3)

# TEST CASE 2
# Enter a sentence: i go to CPP i enjoy CPP i learn at CPP i exercise at CPP   
# Dictionary: {'i': 4, 'go': 1, 'to': 1, 'CPP': 4, 'enjoy': 1, 'learn': 1, 'at': 2, 'exercise': 1}
# 1st Most Frequent Element: ('CPP', 4)
# 2nd Most Frequent Element: ('i', 4)
# 3rd Most Frequent Element: ('at', 2)



# --------------------- TASK 2 ---------------------
# form two lists with list comprehension
L1 = [random.randrange(1, 100) for i in range(100)]
L2 = [i for i in range(1, 100) if i % 3 == 0 or i % 4 == 0]

# form sets from lists
S1 = set(L1)
S2 = set(L2)

# create sets using S1 and S2
R1 = S1.union(S2)
print("R1 (Union):", R1)
print("R1 Size:", len(R1))

R2 = S1.intersection(S2)
print("R2 (Intersection):", R2)
print("R2 Size:", len(R2))

R3 = S1.difference(S2)
print("R3 (Difference):", R3)
print("R3 Size:", len(R3))

# OUTPUT: 

# TEST CASE 1
# R1 (Union): {1, 2, 3, 4, 6, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 36, 37, 39, 40, 41, 42, 44, 
# 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 
# 87, 88, 90, 91, 92, 93, 95, 96, 97, 99}
# R1 Size: 79
# R2 (Intersection): {6, 12, 15, 20, 21, 24, 27, 28, 30, 36, 39, 40, 42, 44, 45, 48, 51, 52, 54, 56, 57, 60, 63, 64, 69, 80, 84, 87, 88, 90, 92}
# R2 Size: 31
# R3 (Difference): {1, 2, 10, 13, 14, 19, 25, 26, 29, 31, 37, 41, 46, 49, 50, 55, 58, 59, 65, 67, 70, 73, 74, 77, 82, 83, 85, 91, 95, 97}
# R3 Size: 30

# TEST CASE 2
# R1 (Union): {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 
# 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 63, 64, 65, 66, 68, 69, 70, 71, 72, 75, 76, 78, 79, 80, 81, 82, 83, 84, 87, 
# 88, 89, 90, 92, 93, 94, 96, 97, 98, 99}
# R1 Size: 83
# R2 (Intersection): {9, 12, 16, 18, 20, 21, 24, 28, 30, 32, 33, 36, 44, 45, 51, 57, 60, 63, 64, 66, 69, 76, 78, 81, 84, 87, 88, 90, 93, 96, 99}
# R2 Size: 31
# R3 (Difference): {1, 2, 5, 7, 10, 11, 13, 17, 22, 29, 31, 34, 35, 37, 38, 41, 43, 46, 47, 49, 50, 53, 55, 59, 65, 70, 71, 79, 82, 83, 89, 94, 97, 98}
# R3 Size: 34
