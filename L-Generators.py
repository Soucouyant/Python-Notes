# Duran Ramlall 
# Learn Python - Generators
# Tuesday May 10 2022 
# TEJ4M1 P2

# Generators are used to create custom iterators
# We can create a new generator by making a function
# Instead of using a return statement, which stops the codes execution, we can use the yield statement which pauses the function until it's next call
def range():
    i = "Hello"
    yield i
    j= "My"
    yield j
    k = "Name"
    yield k
    l = "is"
    yield l
    m = "Duran"
    yield m
    

rangeCall = range()
print(next(rangeCall))
print(next(rangeCall))
print(next(rangeCall))
print(next(rangeCall))
print(next(rangeCall))

# In the function range, we have various variables containing a piece of an introduction
# After each variable declaration we yield the variable
# This is similar to a return statement in the sense that it provides a value to the call, however, it doesn't fully terminate the function, it just pauses it
# using the next() function, which moves to the next item in an iterator, we keep printing each called variable
