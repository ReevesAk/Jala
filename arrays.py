def add_int_values():
    n_list = [1, 2, 3]
    total = 0
    for item in range(0, len(n_list)):
        total = total + n_list[item]
    print("sum of integer values: ", total)


add_int_values()


def avg_Val():
    n_list2 = [1, 2, 3]
    total = 0
    for item in range(0, len(n_list2)):
        total = total + n_list2[item]
    print("average value of array: ", total / len(n_list2))


avg_Val()

num_list = [1, 2, 3]
if 2 in num_list:
    value_index = num_list.index(2)
    print(value_index)


def array_contains(n):
    num_list2 = [1, 2, 3]
    for _ in num_list2:
        if n in num_list2:
            print("item is present in array")
            break
        else:
            print("item is absent in array")
            break


array_contains(1)


def remove_item():
    numlist = [1, 2, 3]
    numlist.remove(2)
    print(numlist)


remove_item()


def copy_array():
    num_list3 = [1, 2, 3]
    new_list = num_list3.copy()
    print(new_list)


copy_array()


def insert_element():
    numlist = [1, 2, 3]
    numlist.insert(4, 2)
    print(numlist)


insert_element()


def max_and_min():
    num_list4 = [1, 2, 3]
    mx = max(num_list4)
    mn = min(num_list4)

    print(f"{mx} is the maximum value while {mn} is the minimum value")


max_and_min()


def reverse_list():
    num_list5 = [1, 2, 3]
    num_list5.reverse()
    print(num_list5)


reverse_list()


def duplicate():
    num_list6 = [1, 2, 3]
    if len(num_list6) == len(set(num_list6)):
        print("Yes, list contains duplicates")
    else:
        print("No duplicates found in list")


duplicate()


def common_values(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    print(result)


num_list7 = [1, 2, 3]
num_list8 = [9, 4, 3]
common_values(num_list7, num_list8)


class List(object):
    def remove_duplicate(self, list1, list2):
        for element in list1:
            if element in list2:
                list1.remove(element)
        print(list1)

    def secondlargest(self):
        num_list9 = [1, 2, 3]
        num_list9.sort()
        print("Second largest element is:", num_list9[-2])

    def even_or_odd(self):
        i = 0
        while i < len(num_list7):
            if i % 2 == 0:
                print(i, "is even")
            else:
                print(i, "is odd")
            i += 1

    def find_two_specific_element(self, n1, n2):
        num_list10 = [1, 2, 3]
        for _ in num_list10:
            if n1 and n2 in num_list10:
                print("items are present in array")
                break
            else:
                print("items are absent in array")
                break


def difference_btw_max_and_min():
    num_list11 = [1, 2, 3]
    mx = max(num_list11)
    mn = min(num_list11)

    print(mx - mn)


def remove_duplicate_and_return_new_array():
    num_list12 = [1, 2, 3, 2]
    new_array = []
    for i in num_list12:
        if i not in new_array:
            new_array.append(i)
    print(new_array)


n1 = [2, 3, 5, 7]
n2 = [1, 5, 8, 4]

myclass = List()
myclass.remove_duplicate(n1, n2)
myclass.secondlargest()
myclass.evenorodd()
difference_btw_max_and_min()
myclass.find_two_specific_element(12, 23)
remove_duplicate_and_return_new_array()
