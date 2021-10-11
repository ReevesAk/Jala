print("My name is Reeves")

# This is a single line comment.

"""
This is to demonstrate a multiline
comment. I am telling the compiler 
to ignore this few lines.
"""

myAge = 27
isShort = False
firstLetter = "R"
pi = 3.142

print(myAge, isShort, firstLetter, pi)

name = "Shiva"


def printname():
    global name
    name = "Shiva Jala"


# Shiva prints before printName function is called.
print(name)

printName()
# Shiva Jala prints after printName function is called.
print(name)
