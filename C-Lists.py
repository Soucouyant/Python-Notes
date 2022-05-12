# Duran Ramlall 
# Learn Python - Lists
# Friday May 6 2022 
# TEJ4M1 P2

# Declaration
## Similar to Arrays
## Fundamnetally different from Arrays in "statically" typed languages
## No reference type
## Lists can hold any type or variable or any amount of variables (as long as memory permits)
newList = []

# Adding a value
# Use the append method
newList.append("Duran")
newList.append(2)
print(newList)

# Iterating through List
# Using for each loop / enchanced for loop
for x in newList:
    print(x)
# Note that indentation matters
# Also, x will copy each element in the array, x does not correspond to an actual element

# Bugs
# Trying to access an index that does not exist will result in an erorr
# Ex.
# print(newList[5]) 
# Since newList only has 2 elements, with the highest index of 1, an index of 5 does not exist