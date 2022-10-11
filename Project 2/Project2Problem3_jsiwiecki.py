# Author: Joseph Siwiecki
# Assignment: Project 2 Problem 3
# Completed: 10/10/2022
# Class: CS 2520.01

# --------------------- PROBLEM 3 ---------------------
def encode_zip_code(zip_code):
    barcode = "┃"
    
    zip_code = zip_code.replace("-", "")
    zip_code = int(zip_code)
    check_sum = (10 - (sum([int (d) for d in str(zip_code)]) % 10))

    check_sum = str(check_sum)
    zip_code = str(zip_code)
    zip_code += check_sum
    
    for i in range(len(zip_code)):
        char = zip_code[i]
        
        match char:
            case '0':
                barcode += "┃┃╻╻╻"
            case '1':
                barcode += "╻╻╻┃┃"
            case '2':
                barcode += "╻╻┃╻┃"
            case '3':
                barcode += "╻╻┃┃╻"
            case '4':
                barcode += "╻┃╻╻┃"
            case '5':
                barcode += "╻┃╻┃╻"
            case '6':
                barcode += "╻┃┃╻╻"
            case '7':
                barcode += "┃╻╻╻┃"
            case '8':
                barcode += "┃╻╻┃╻"
            case '9':
                barcode += "┃╻┃╻╻"
                 
    barcode += "┃"
    
    return barcode

def main():
    zip_code = input("Enter a zip code: ")
    print(encode_zip_code(zip_code))
    
main()

# OUTPUT:
# TEST CASE 1
# Enter a zip code: 55555-1237
# ┃╻┃╻┃╻╻┃╻┃╻╻┃╻┃╻╻┃╻┃╻╻┃╻┃╻╻╻╻┃┃╻╻┃╻┃╻╻┃┃╻┃╻╻╻┃╻╻┃╻┃┃

# TEST CASE 2
# Enter a zip code: 91768-1234
# ┃┃╻┃╻╻╻╻╻┃┃┃╻╻╻┃╻┃┃╻╻┃╻╻┃╻╻╻╻┃┃╻╻┃╻┃╻╻┃┃╻╻┃╻╻┃┃╻┃╻╻┃

# TEST CASE 3
# Enter a zip code: 20500-0000
# ┃╻╻┃╻┃┃┃╻╻╻╻┃╻┃╻┃┃╻╻╻┃┃╻╻╻┃┃╻╻╻┃┃╻╻╻┃┃╻╻╻┃┃╻╻╻╻╻┃┃╻┃
