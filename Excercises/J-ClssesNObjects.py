# Duran Ramlall 
# Learn Python - Classes and Objects
# Tuesday May 17 2022
# TEJ4M1 P2

# define the Vehicle class
class Vehicle:
    def __init__(self, color, kind, name, value):
        self.color = color
        self.kind = kind
        self.name = name
        self.value = value
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle("red", "convertible", "Fer", 60000.00)
car2 = Vehicle("blue", "van", "Jump", 10000.00)

# test code
print(car1.description())
print(car2.description())