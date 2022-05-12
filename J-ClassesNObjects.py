# Duran Ramlall 
# Learn Python - ClassesNObjects
# Sunday May 8 2022 
# TEJ4M1 P2

# Classes and Objects are at the heart of OOP (Object Oriented Programming)
# It is the staple for languages like Java, and is the base principle for many programs used today
# OOP is possible within python due to its built in support for Classes and Objects

# Objects are entities that have a list of properties (variables) and methods (functions) that can be used with them
# Classes are the template to create objects

# For example, we can have a bank account class which defines a balance variable as well as two methods to deposit and withdraw money
# We can use this bank account class to create Duran Ramlall's bank account (which is an object), which will have it's own balance which are effected differently by the two methods
# We can keep creating new bank account objects which will act differently, but still have the same base template

# Class
# We can define a class by using the "class" keyword
class bankAccount:
    balance = None
    # None keyword means that the balance is equal to null, not exactly zero, it just has no value
    def deposit(amount):
        balance += amount
        print("You have deposited $" + amount + ". The new balance is $" + balance)
    def withdraw(amount):
        balance -= amount
        print("You have withdrawn $" + amount + ". The new balance is $" + balance)
# While this may be a proper class, our balance would be None
# None is a special datatype, and we cannot add to it using regular ints or floats
# So how do we let the user define their starting balance?
# We could use he init() function

# Within classes, the init() function has a special property. It can define values when a new object is created using our class 
class bankAccount2:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
# Now, when a user creates a bank account they can define their own starting value
# Within the init() function, the first parameter always references the current instance of the class (meaning the instance that is used by an object)
# It does not have to be named self, but it makes sense syntaxically

# Now that we have a bankAccount class, we can start making users
# We can create an object like so
DuranRamlall = bankAccount2(200)
# We made a variable called DuranRamlall, and referenced the class bankAccount2, therefore making DuranRamlal an object
# Now that DuranRamlall is an object, it creates a copy of the bankAccount2 class that is completely unqiue to DuranRamlall
User2 = bankAccount2(100)

# We can access a varaible within a class using the dot (.) operator
print(DuranRamlall.balance)
print(User2.balance)
# Note that despite using the same class, the balances are unique, making each object a new instance of the class

# Similarly if we wanted to use the functions in a class we can use the dot operator
DuranRamlall.deposit(50)
print(DuranRamlall.balance)