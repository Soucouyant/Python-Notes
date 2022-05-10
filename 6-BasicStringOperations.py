# Duran Ramlall 
# Learn Python - Basic String Operations
# Saturday May 7 2022 
# TEJ4M1 P2

# Printing and Adding Strings are somewhat useful
# However, there is much more than can be done with Strings

# Strings can be formed with "" (double quotes) or '' (single quotes)
# However, with single quotes, apostrophes (don't, can't, won't) cannot be done
# The reason for this is because python will interpret the second single quote it sees as the end of a String

print('Hello, World!')
# print('I can't do that) Uncommenting this code will result in an error on execute

print("I can't do this, well I can now!") 
# This works though, as it interprests the second double quote as the end

# Methods
# the len() method returns the length of the string (including punctuation and spaces)
print(len("Hello")) # Output: 5
print(len("My name is Duran")) # Output 16

# the index() method returns the first occurence of a given char or sequence
stringA = "My name is Duran"
print(stringA.index("n")) # Ouput: 3
# This method returns 3 because the first occurence of n is index 3 away from the beginning
# The first character in the string is index 0, and then increases per character
stringB = "My name is Duran" 
print(stringB.index("Du")) # Output: 11
# This returns 11 because the sequence "Du" appears as the 11th index 
# This method groups the search string ("Du") and recognizes it as one index item therefore it counts as 1 item


# the count() method returns the number of times a search string occurs within the given string
stringC = "This is the third string"
print(stringC.count("r")) # Output: 2
print(stringC.count("t")) # Output: 3
# You may recognize the output as incorrect because in stringC there are 4 t's
# the count() method counts the literal of what the search string is
# In essence, the fourth t is T, and in python (and most other languages) t /= T
# Python doesn't count recognize T as t 

# String Slicing
# By using square brackets beside the variable name of the string and values in it you can slice the string
# Negative values can be used and they represent from the end, whereas positive start from the beginning
stringD = "This is the fourth string"
print(stringD[3:9])
# The colon represents the word "to" 
# The statement translates to "print index 3 to 9 of stringD"

print(stringD[3])
# This statement prints index 3

print(stringD[-3])
# This statement prints index 3 from the end

print(stringD[3:9:5])
# This statement prints s and then index 5 (t)

print(stringD[::-1])
# This statement reverses the string

# Upper and Lower Case
# By using the upper() and lower() methods you can convert a string to all uppercase or lowercase
stringE = "This is the fifth string"
print(stringE.upper())
print(stringE.lower())

# startswith() and endswith() 
# These methods return a boolean value for if a string starts or ends with a string
stringF = "This is the sixth string"
print(stringF.startswith("This"))
print(stringF.endswith("string."))
# You may be confused as to why statement two return False
# Once again the input string is a literal, the string doesn't end with a period.

# split() method 
# The split method splits the string at the given input
# The method returns a list with the split elements
stringG = "Split here"
splitWords = stringG.split(" ")
print(splitWords)
