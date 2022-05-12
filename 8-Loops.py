# Duran Ramlall 
# Learn Python - Loops
# Saturday May 7 2022 
# TEJ4M1 P2

# There are two main loops for and while
# For loops iterate over a given list
listA = [1,2,3,4,5]
for numbers in listA:
    print(numbers)
# This will output all the numbers in the list on a seperate line
# This works because the numbers variable is being used as a copy for each element in the array
# Since the numbers variable is essentially a copy of the element, it does not modify the list in any way

# range
# For loops can also be used with the range function
# There are 3 possible parameters.
# (start, stop, step)
# the step value isn't necessary, but both the start and stop value are.
for x in range(3,8,2):
    print(x)

# While loops
# while loops will repeat as long as a condition is met
i = 0
while i < 5: 
    print(i)
    i += 1
# The while loop will run as long as 5 is less than 5
# I use the variable i as a count to manage the loop, and to avoid a infinite while loop

# break
# The break keyword will "break" the loop, meaning that the loop will stop once python executes it
# This can be used for either a for or while loop
j = 0 
while j != 2:
    print(j)
    j += 1
    if j == 2:
        break
# When run, this loop will display 0 and 1, before breaking when j = 2

# continue
# The continue keyword skips the current iteration of the loop
# Again this can be used with either a for or a while loop
status = ["Done","In Progress", "Quit"]
for name in status: 
    if name == "In Progress":
        continue
    print(name)
# This will output only Done and Quit because if the name value is equal to "In Progress" the iteration is skipped before it can be printed

# else statements
# An important thing to note is that else statements can be used in loops
k = 0 
while k < 3:
    print(k)
    k += 1
else:
    print("K is equal to 3")
# Once k is equal to 3 and the while loop confition isn't true, the else statement is executed