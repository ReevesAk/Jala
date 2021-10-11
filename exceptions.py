# Program to generate Arithmetic Exception without exception handling.
# arithmetic_error = 10 / 0
# print(arithmetic_error)
from json import qwerty
import sys

try:
    arithmetic_error = 10 / 0
except ArithmeticError:
    print("there is an error")


class Exceptions:
    def __int__(self):
        pass

    # Method that throws exception.
    def throw_exceptions(self):
        print(10 / 0)


# Program to throw error and catch multiple exceptions.
num0 = 10

try:
    num1 = input("Enter 1st number:")
    num2 = input("Enter 2nd number:")
    result = (int(num1) * int(num2)) / (num0 * int(num2))
except ValueError as v_err:
    print(v_err)
    exit()
except ZeroDivisionError as zero_err:
    print(zero_err)
    exit()
except TypeError as type_err:
    print(type_err)
    exit()
except:
    print('Unexpected Error!')
    exit()


# Program to draw exception in my own words.
class Error(Exception):
    pass


class LowError(Error):
    pass


class HighError(Error):
    pass


try:
    user_input = int(input("Enter a number:"))
    if user_input < 10:
        raise LowError
    elif user_input < 10:
        raise HighError
except LowError:
    print("the entered number is less than what is required")
except HighError:
    print("the entered number is higher than what is required")

# Program with finally block.
try:
    arithmetic_error = 10 / 4
except ArithmeticError:
    print("there is an error")
finally:
    print("Program executed successfully!!!")

# FileNotFound Exception.
with open("stack.txt", "r") as f:
    content = f.read()
    print(content)

try:
    f = open("foo.txt", 'r')
except IOError as e:
    print(e)
    print(sys.exc_type)


if __name__ == '__main__':
    exceptions = Exceptions()
    exceptions.throw_exceptions()
