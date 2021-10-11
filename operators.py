def arithmeticoperators():
    add = 7 + 3
    sub = add - 0
    div = sub / 2
    times = div * 5
    print(times)


arithmeticoperators()


def increment(num):
    num += num
    print(num)


def decrement(num):
    num -= num
    print(num)


increment(5)
decrement(10)


def equalornot(num1, num2):
    if num1 == num2:
        print("they are equal")
    else:
        print("they are not equal")


equalornot(5, 9)


def relationaloperators(num1, num2):
    if num1 == num2:
        print("they are equal")
    elif num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        pass
    return


relationaloperators(10, 5)


def smallerandlarger(num1, num2):
    if num1 > num2:
        print(f"{num1} is the larger number and {num2}, is the smaller number")
    elif num1 < num2:
        print(f"{num2} is the larger number and {num1}, is the smaller number")
    else:
        pass
    return


smallerandlarger(6, 20)
