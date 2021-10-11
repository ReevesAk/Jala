# Operations on files using Python.
import os

# Reading a text file.
with open("caro.txt", "r") as f:
    content = f.read()
    print(content)

# Writing text to .txt file using input()
print('Enter your names')
inputName = input()
with open('name.txt', 'w') as f:
    f.write(inputName)

# Program to read a file stream.
with open("name.txt", "r") as f:
    content = f.read()
    print(content)

# Program to read a file to an index.
with open("name.txt", "r") as f:
    f.seek(7)
    print(f.readline())

    f.close()

# Check if a file has read access.
print(os.access('name.txt', os.R_OK))

# Check if a file has write access.
print(os.access('name.txt', os.W_OK))
