# input: {a:2, b:3, c:4}, {a:1, b:2, d:6}
# output: {a:[2,1], b:[3,2], c:[4],d:[6]}


def str_to_list_to_dict():
    dictionary = {}
    key = []
    value = []
    keys = input("enter the keys for a dict: ")
    keys_lists = [x for x in keys]
    key.extend(keys_lists)
    keys_lists.clear()
    values = input("enter the value for a dict: ")
    values_list = [x for x in values]
    value.extend(values_list)
    zip(key, value)
    for key, value in zip(key, value):
        dictionary[key] = int(value)
    return dictionary

dictionaries = {}
def dict_fun(dict1, dict2):

    for i in [dict1,dict2]:
        for k,v in i.items():
            output_of_the_get = dictionaries.get(k, None)
            if output_of_the_get is None:
                if isinstance(v, list):
                    dictionaries[k] = v
                else:
                    dictionaries[k] = [v]
            else:
                if isinstance(v, list):
                    dictionaries[k].extend(v)
                else:
                    dictionaries[k].append(v)
    return {k:set(v) for k,v in dictionaries.items()}

#
# dict1 = str_to_list_to_dict()
# dict2 = str_to_list_to_dict()
# print(dict_fun(dict1, dict2))

def dict(a,b,c):
    dict1 = {}
    for i in [a,b,c]:
        for k, v in i.items():
            output_of_get = dict1.get(k, None)
            if output_of_get is None:
                if isinstance(v, list):
                    setv = set(v)
                    dict1[k] = setv
                else:
                    dict1[k] = {v}
            else:
                if isinstance(v, list):
                    set1 = set(v)
                    dict1[k] = dict1[k].union(set1)
                else:
                    set2 = set(v)
                    dict1[k].add(set2)
    return dict1

a = {"a":[1], "b":[2,3], "c":3}
b = {"a":[7], "b":[5,6], "d":9}
c = {"h":[7], "z":[5,6], "x":[111]}

# print(dict_fun(a,b))
#
# dict1 = {k:set(v) for k,v in c.items()}
# print(dict1)


def reverse(string):
    if len(string) <= 1:
        return string
    return reverse(string[1:]) + string[0]

reverse_str = reverse("hello")
print(reverse_str)















