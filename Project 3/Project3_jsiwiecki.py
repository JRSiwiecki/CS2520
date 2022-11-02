# Author: Joseph Siwiecki
# Assignment: Project 3
# Completed: 11/2/2022
# Class: CS 2520.01

# --------------------- TASK 1 ---------------------

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
        
        # replace unnecessary characters
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
        
        # print 10 most frequent words
        for i in range(len(dict)):
            print(dict[i])
            count += 1
            
            if count == 10:
                break
            
        file.close()

# --------------------- TASK 2 ---------------------
def task_2(): 
    
    # helper function
    def is_prime(n):
        for i in range(2 ,int( (n ** 0.5)) + 1):
            if n % i == 0:
                return False
        return True

    # prime generator
    def get_primes(n):
        yield 2
        i = 1
        count = 1
        while count < n:
            i += 2
            if is_prime(i):
                count += 1
                yield i
    
    # fibonacci generator
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    L1 = [x for x in get_primes(100)]
    L2 = [x for x in fib(100)]
    
    S1 = set(L1)
    S2 = set(L2)
    
    # create sets using S1 and S2
    R1 = S1.union(S2)
    # print("R1 (Union):", R1)
    print("R1 Size:", len(R1))

    R2 = S1.intersection(S2)
    # print("R2 (Intersection):", R2)
    print("R2 Size:", len(R2))

    R3 = S1.difference(S2)
    # print("R3 (Difference):", R3)
    print("R3 Size:", len(R3))
