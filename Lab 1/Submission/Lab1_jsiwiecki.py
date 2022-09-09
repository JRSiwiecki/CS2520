print("Welcome to the Ice Cream Store")

print("Alvin's purchase:")
eachScoop = 2 # $2 each scoop of ice cream
bought = 3 # bought 3 scoops of ice cream
print("Alvin needs to pay", eachScoop * bought, "dollars")

print("Now Terri is buying ice cream.")
choice = (int(input("Do you want chocolate or vanilla? 1 for chocolate, 2 for vanilla: ")))

if choice == 1:
    iceCreamName = "chocolate"
else:
    iceCreamName = "vanilla"

eachScoop = (int(input("Please enter how much each scoop costs: ")))
bought = (int(input("How many scoops did you buy? ")))
print("Terri needs to pay", eachScoop * bought, "dollars for their " + iceCreamName + " ice cream.")

# Welcome to the Ice Cream Store
# Alvin's purchase:
# Alvin needs to pay 6 dollars
# Now Terri is buying ice cream.
# Do you want chocolate or vanilla? 1 for chocolate, 2 for vanilla: 1
# Please enter how much each scoop costs: 1
# How many scoops did you buy? 3
# Terri needs to pay 3 dollars for their chocolate ice cream.
