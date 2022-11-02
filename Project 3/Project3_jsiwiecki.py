# Author: Joseph Siwiecki
# Assignment: Project 3
# Completed: 11/2/2022
# Class: CS 2520.01

# --------------------- TASK 1 ---------------------
# ----------- PART 1 -----------

def task_1():
    try:
        file_name = input("Enter the name of the file (no extension): ")
        file_name = file_name.strip() + ".txt"
        
        # need to use utf-8 encoding because otherwise, can't be parsed properly
        file = open(file_name, encoding="utf8")
    except FileNotFoundError:
        print("File not found!")
    else:
        dict = {}
        
        sentence = file.read()
        sentence = sentence.replace(',', '')
        sentence = sentence.replace('.', '')
        sentence = sentence.replace('\"', '')
        sentence = sentence.replace('\'', '')
        sentence = sentence.replace("—", '')
        words = sentence.split()
        
        for word in words:
            if word in dict:
                dict[word] = 1 + dict[word]
            else:
                dict[word] = 1
            
        # sort dictionary by keys
        dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        
        count = 0
        
        for i in range(len(dict)):
            print(dict[i])
            count += 1
            
            if count == 10:
                break
            
        file.close()

# --------------------- TASK 2 ---------------------
def task_2():
    print()



task_1()