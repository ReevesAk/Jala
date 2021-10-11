for _ in range(10):
    print("Bright IT Career")

i = 1
while i < 21:
    print(i)
    i += 1


def equal_or_not(a, b):
    is_not_equal = a != b
    print(is_not_equal)


equal_or_not(5, 5)


def even_or_odd(n):
    if n % 2 == 0:
        print(f"{n} is an even number")
    else:
        print(f"{n} i an odd number")


even_or_odd(9)


def largest_num(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    print("The largest number is", largest)


largest_num(4, 17, 10)


def even_num():
    i = 9
    while i < 21:
        if i % 2 == 0:
            print(i)
        i += 1


even_num()


def armstrong_or_not(num):
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


armstrong_or_not(153)


def prime_num(num):
    if num > 1:
        for index in range(2, int(num / 2) + 1):
            if (num % index) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")


prime_num(5)


def isPalindrome(s):
    return s == s[::-1]


s = "radar"
result = isPalindrome(s)

if result:
    print("It is palindrome")
else:
    print("It is not a palindrome")


# Python has no switch statment.
def evenorodd():
    i = 9
    while i < 21:
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
        i += 1


evenorodd()


def malefemale(gender):
    if gender == "f":
        print("Female")
    elif gender == "m":
        print("Male")
    else:
        print("You didn't enter a valid character")


malefemale("m")
