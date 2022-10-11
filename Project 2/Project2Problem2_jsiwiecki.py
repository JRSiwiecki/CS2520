# Author: Joseph Siwiecki
# Assignment: Project 2 Problem 2
# Completed: 10/10/2022
# Class: CS 2520.01

import timeit
# --------------------- PROBLEM 1 ---------------------

# ----------- PART 1 -----------
def primes(start, end, printAll):
    
    prime = [True for i in range(end + 1)]
    
    p = 2
    while (p * p <= end):
        
        if (prime[p] == True):
            for i in range(p * p, end + 1, p):
                prime[i] = False
        
        p += 1
    
    if printAll:
        for p in range(start, end + 1):
            if prime[p]:
                yield p
    
    else:
        for p in range(start, end + 1):
            if prime[p] and (p == 547 or p == 8837):
                yield p
    
    
# ----------- PART 2 ----------- 
def main():
    print("--- 100 Primes ---")
    print(*primes(2, 541, True))
    
    print("\n--- 101st to 1100th Primes ---")
    start = timeit.default_timer()
    print(*primes(547, 8837, False))
    stop = timeit.default_timer()
    print()
    
    print("Time to run: ", stop - start)

main()

# OUTPUT: 
# TEST CASE 1
# --- 100 Primes ---
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541

# --- 101st to 1100th Primes ---
# 547 8837

# Time to run:  0.0008726000087335706