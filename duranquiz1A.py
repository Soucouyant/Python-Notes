# Duran Ramlall
# Thursday May 12 2022
# Quiz 1A
# TEJ4M1 P2

firstNumber = 15
secondNumber = 19

wordList = [
    "Sword", 
    "Apple", 
    "Pen", 
    "Brave", 
    "Strong", 
    "Weak", 
    "Keyboard", 
    "Mouse"
]

ints = (firstNumber, secondNumber)
formattedString = "The first number is %d, the second number is %d,"
print(formattedString %(ints), "and the list with words is: ", wordList)

while firstNumber > -1:
    print(firstNumber)
    firstNumber -= 1
    
    
charCount = 0
for words in wordList:
    if len(words) <= 4:
        print(words)
    elif len(words) == 5:
        print("This word is perfect.")
    else:
        print("I don't like this word!")
    charCount += len(words)
print("The total number of characters in all the words is: %d." %(charCount))

print("Finished")
