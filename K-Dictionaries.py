# Duran Ramlall 
# Learn Python - Dictionaries
# Tuesday May 10 2022 
# TEJ4M1 P2

# Dictionaries are similar to lists/Arrays
# They hold multiple vlaues, however, with a key and a value instead of just a value
# Instead of using the index number of an element or the value of an element we can instead use it's key to do our various operations

# There are two ways to define a dictionary
from typing import final


method1 = {}
method1["test1"] = 123
method1["test2"] = 456
print(method1)
# In this method we initialize an emoty dictionary, and then add an entry per line
# We can also define a dictionary by giving a set of values initially
method2 = {
    "test1": 123,
    "test2": 456
}
print(method2)

# Both methods yield the same result, the usage depeneds entirely on the individual scenario in which you use a dictionary

# Similar to lists, we can iterate through a dictionary
# However, the key-value pairs aren't ordered in the same way a list is 
userList = {
    "user1": 10,
    "user2": 120
}
for users, age in userList.items():
    print(users, age) 

# Deleting a value
# We can delete a value from a dictionary in 2 ways
# using pop() or del
finalDictionary = {
    "t1": 2,
    "t2": 3,
    "t3": 4,
    "t4": 5
}
del finalDictionary["t1"]
# deletes t1 entry in the dictionary

finalDictionary.pop("t2")
# deletes t2 entry in the dictionary