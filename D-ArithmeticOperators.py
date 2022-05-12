# Duran Ramlall 
# Learn Python - Arithmetic Operaators
# Friday May 6 2022 
# TEJ4M1 P2

# Basic Math
# * | multiplication
# / | division
# + | addition
# - | subtraction
# Python also follows order of operations (BEDMAS)
number = (1+2) * 2  # Expected Output: 6
print(number)       # Output: 6

# Intermediate Operations
# Modulo | % 
# Tells us the remainder after a division operation
number2 = 4 % 2     # Expected Output: 0
print(number2)      # Output: 0
# 4 can be divided into 2 a toal of 2 times, leaving no remaider

# Powers
# ** | Signifies a power
number3  = 2 ** 2   # Expected Output: 4
print(number3)      # Ouput: 4

# String Concatenation
# You can add strings together or specify an amount of times to print the string
# Addition
stringOne = "Hello"
stringTwo = "World"
print(stringOne + stringTwo)

# Multiplication
stringThree = "No " * 5
print(stringThree)

# Lists
# Can be added together
# Addition simply appends the lists
# Not Sorted
multiplesOfFive = [5, 10, 15, 20]
multiplesOfTwo = [2, 4, 6, 8]
totalList = multiplesOfFive + multiplesOfTwo
print(totalList)

# Lists can also be multiplied together
# Multiplication works by appending the list x number of times
oneToFive = [1,2,3,4,5]
print(oneToFive * 2) 
