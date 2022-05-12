# Duran Ramlall 
# Learn Python - Conditons
# Saturday May 7 2022 
# TEJ4M1 P2

# In order to test conditions Python uses booleans
valueOne = 3
print(valueOne == 2) # Output: False

# Comaparative Operators
# == | equals to
# != | does not equal to 
# >  | Greater than
# <  | Less than
# These operators compare two values with the same datatype 

valueTwo = 2
print(valueTwo > valueOne) # Output: False
# This returns false because valueTwo isn't greater than valueOne

# if statement
# In order to execute some code using a condition the "if" statement is used
if valueOne == valueTwo:
    print(valueOne)
# This will not print anything because valueOne does not equal valueTwo
# The statement states that "if valueOne equals valueTwo do something" 

# else statement
# This statement can only be used within a conditional block aka in a sequence of if statements
# You can only use this after one or more if statements
if valueOne == valueTwo:
    print("valueOne equals valueTwo")
else: 
    print("Nothing")
# The translation of this is if valueOne equals valueTwo print a statement else (if this statement is not true) then pring something else

# elif 
# This statement means else if 
# This is used after an if statement to check if another conditional is true
if valueOne == valueTwo:
    print("valueOne equals valueTwo")
elif valueOne != valueTwo:
    print("valueOne does not equal valueTwo")

# in operator
listOne = ["One","Two","Three"]
stringValue = "One"

if stringValue in listOne:
    print("The value is present")
# The operator states that if stringValue is present in listOne then do something

# is operator
# This is similar to the == comparision but fundamentally different
# This comparison checks the instances rather than the actual value
x = [1,2,3]
y = [1,2,3]
z = x 
print(x == y)  # Output: True
print(x is y)  # Output: False
print(x is z ) # Output: True
# This returns true because we defined z as equal to x, meaning their instances are he same
# Whereas in the second statement x is not y even if the values are the same, they both have different memory addresses and therefore are seperate entities

# not operator
# This inverts the value of a boolean expression
print(not False) # Output: True