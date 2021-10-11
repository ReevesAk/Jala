import re

# 1. Ways to create a string.
n = "Muna"
n2 = 'Reeves'
# 2. Concatenating two strings using + operator.
print(n, n2)


print("It is rare to see Reeves " + "drink beer")

# 3. Finding the length of the string
print(len(n))
# 4. Extract a string using Substring
print(n2[0:3])

# 5. Searching in strings using index().
print(n2.index("v"))

# 6. Matching a String Against a Regular Expression With matches().
regular = "It is rare to see Reeves eat catfish"
result = re.search(n2, regular)
if result:
    print("match was found")
else:
    print("match wasn't found")    


# 7. Comparing strings.
if n == n2:
    print(True)
else:
    print(False)    

# 8. StartsWith(), endsWith() compareTo()
if n2.startswith("R") and n2.endswith("s"):
    print("Hurray, it is Reeves")
else:
    pass


if n != n2:
    print(n, "is not the same when compared to", n2)
else:
    pass   


# 9. Trimming strings with strip().
string = " Arero "
strip = string.strip()
print(strip)

# 10. Replacing characters in strings with replace().
n = n.replace("a", "e")
print(n)

# 11. Splitting strings with split().
split = n2.split("e", 3)
print(split)

# Converting integer objects to Strings.
num = 10
str(num)
print(type(num))

# 13. Converting to uppercase and lowercase.
upp = "REEVES"
low = "akwa"

upp = upp.lower()
low = low.upper()

print(low)
print(upp)

