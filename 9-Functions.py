# Duran Ramlall 
# Learn Python - Functions
# Sunday May 8 2022 
# TEJ4M1 P2

# Functions
# They are a way of dividing your code into their own repeatable blocks
# There are two main actions to do with functions, creating and calling

# Creating a function - def
# We can use the def keyword to create a function
def functionOne():
    print("x")
# We have created a function called functionOne, note that the () are necessary in order to make it a function
# The () beside the function name is where we define our "parameters"
# Function parameters are used when our function needs extra data in order to run it's code
# For example, if we wanted a function that added $10 to our wallet, we would need the initial value to return the value after $10 has been added
def functionTwo(x):
    print(x)
# The function above requires the paramater "x" and will print the parameter "x" 
# Note that we will have to use unique names for parameters within the function 
# Also, the variables are local to the function, meaning that they cannot be used outside the function

# return statements
# The return statement is a statement that returns something when the function is called
# return statements aren't always necessary since functions can manipulate variables outside of it's scope
# However, if the function needs to calculate something that we need, a return statement is necessary 
def functionThree(x,y):
    return x + y 
# Once we pass two numbers into this function it will return the sum of both numbers

# Calling a function
# Once we create a function we have the option to call it, or basically, use it
def printHello():
    print("Hello")
# In order to call a function we must type the name of the function (literal) with the parenthesis
printHello()

# Note that if our functions have parameters, they must be defined within the function call in the parenthesis
def addNum(x,y):
    print(x+y)

addNum(1,2)

# We can also call functions as equal to a variable
def multiplyTwoNum(x,y):
    return x*y
product = multiplyTwoNum(1,2)
print(product)
# We utilize the return statement to make product = 2