"""
LEGB
Local, Enclosing, Global, Built-in
"""
from tuples import reverse


# Local: a variables that are defined within a function.
# Enclosing: is a local scope enclosing in a function.
# Global: variables which are defined at the top level of the module or explicitly decleared by using the global keyword.
# Built-in: are just pre-assigned by the python.

# Golabal and Local variable
# x = "global x"
def test():
    # global x
    x = "local x"
    # print(y)
    # print(x)

test()
# print(x)
def result(list):
    return set(range(len(list)-1)[1:]) - set(list)


list1 = list(range(1,100))
list1.remove(45)
# print(result(list1))

list5 = [3,4,5,6,9]
list6 = [2,3,5,7,8,9,1]

def intersection(list1,list2):
    result , cpy_list2 = [], list2[:]
    for i in list1:
        if i in cpy_list2:
            result.append(i)
            cpy_list2.remove(i)
    return result


# print(intersection(list5, list6))

def reverse_of_string(string):
    if len(string) == 1:
        return string
    return reverse(string[1:]) + string[0]


# print(reverse_of_string("srinu"))


def reverse_of_string_without_using_reservse_method(string):
    if len(string) == 1:
        return string
    return string[::-1]

# print(reverse_of_string_without_using_reservse_method("srinu"))

num1 = [x for x in range(2,11)]
# def list1(num1):
#     for i in num1:
#         yield i*i
# print1 = list1(num1)
# for i in print1:
#     print(i)

