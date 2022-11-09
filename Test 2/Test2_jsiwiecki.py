# Name: Joseph Siwiecki
# Assignment: Test 2
# Date: 11/8/22

# TASK A B C
def main():
     # ----- TEST CASE 1 -----
    
    weekDays1 = ("Mo", "Tu", "We", "Th", "Fr")
    am1 = [72, 75, 68, 69, 70]
    noon1 = [77, 78, 70, 69, 75]
    pm1 = [71, 76, 72, 65, 73]
    
    dailyTemp1 = list(zip(weekDays1, am1, noon1, pm1))
    print("Daily Temperatures:", dailyTemp1)
    
    avgTemp1 = aveTemp(dailyTemp1)
    print("Average Temperatures: ", avgTemp1)
    
    # ----- TEST CASE 2 -----
    
    weekDays2 = ("Mo", "Tu", "We", "Th", "Fr")
    am2 = [55, 33, 55, 33, 77]
    noon2 = [61, 62, 63, 64, 65]
    pm2 = [1, 2, 3, 4, 5]
    
    dailyTemp2 = list(zip(weekDays2, am2, noon2, pm2))
    print("Daily Temperatures:", dailyTemp2)
    
    avgTemp2 = aveTemp(dailyTemp2)
    print("Average Temperatures: ", avgTemp2)
    
def aveTemp(dailyTempLst):
    averageTemp = []
    
    for i in range(0, len(dailyTempLst)):
        dailyAvgTemp = ((dailyTempLst[i][1] + dailyTempLst[i][2] + dailyTempLst[i][3]) / 3)
        dailyAvgTemp = round(dailyAvgTemp, 1)
        averageTemp.append((dailyTempLst[i][0], dailyAvgTemp))
    
    return averageTemp

main()

# OUTPUT:

# TEST 1
# Daily Temperatures: [('Mo', 72, 77, 71), ('Tu', 75, 78, 76), ('We', 68, 70, 72), ('Th', 69, 69, 65), ('Fr', 70, 75, 73)]
# Average Temperatures:  [('Mo', 73.3), ('Tu', 76.3), ('We', 70.0), ('Th', 67.7), ('Fr', 72.7)]

# TEST 2
# Daily Temperatures: [('Mo', 55, 61, 1), ('Tu', 33, 62, 2), ('We', 55, 63, 3), ('Th', 33, 64, 4), ('Fr', 77, 65, 5)]
# Average Temperatures:  [('Mo', 39.0), ('Tu', 32.3), ('We', 40.3), ('Th', 33.7), ('Fr', 49.0)]
