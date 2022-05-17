# Duran Ramlall 
# Learn Python - Generators
# Tuesday May 17 2022
# TEJ4M1 P2

# fill in this function
from re import I


def fib():
    a, b = 1,1
    while True:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break