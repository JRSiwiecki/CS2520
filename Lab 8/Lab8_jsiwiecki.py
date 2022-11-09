# Author: Joseph Siwiecki
# Assignment: Lab 8
# Completed: 11/1/2022
# Class: CS 2520.01

# --------------------- TASK 1 ---------------------

# create file name variable
try:
    file_name = input("Enter file name (without extension): ")
    file_name = file_name.strip()
    file_name = file_name + ".txt" 
    file = open(file_name, "r")

except FileNotFoundError: 
    print("File Not Found!")

else:
    # get raw data, strip newlines from data
    raw = file.readlines()
    lines = [line.strip() for line in raw]
    lines = tuple(lines)
    data = []
    
    min, max, sum = 100, 0, 0
    minCity, maxCity = "", ""
    
    # convert each line to a list and add that to a list as a tuple
    # convert the number from a string to a float
    # calculate new rainfall values and round
    # also track min, max, and sum
    for i in range(len(lines)):
        line = lines[i].split()
        line[1] = float(line[1])
        line[1] = line[1] * 2.54
        line[1] = round(line[1], 2)
        
        sum += line[1]
        
        if line[1] < min:
            minCity = line[0]
            min = line[1]
        
        if line[1] > max:
            maxCity = line[0]
            max = line[1]
        
        data.append(tuple(line))
        
    
    
    # print statistics
    highest_rainfall = "Highest Rainfall:", maxCity, max, "cm"
    lowest_rainfall = "Lowest Rainfall: ", minCity, min, "cm"
    
    
    print(highest_rainfall)
    print(lowest_rainfall)
    
    mean = sum / len(data)
    mean = round(mean, 2)
    average = "Average Rainfall:", mean, "cm"
    print(average)

    file.close()
    
    new_name = input("Enter the name you want to save the file as (no extension): ")
    new_name = new_name.strip() + ".txt"
    
    new_file = open(new_name, "a+")
    
    # add statistics and scaled data to new file
    for i in range(len(data)):
        new_file.write(str(data[i]))
        new_file.write("\n")
    
    new_file.write(str(highest_rainfall) + "\n")
    new_file.write(str(lowest_rainfall) + "\n")
    new_file.write(str(average) + "\n")
    
    new_file.close()