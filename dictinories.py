# input: {a:2, b:3, c:4}, {a:1, b:2, d:6}
# output: {a:[2,1], b:[3,2], c:[4],d:[6]}




def str_to_list_to_dict(no_of_dicts):

    dictionary = {}
    for i in range(no_of_dicts):
        key = []
        value = []
        keys = input("enter the keys for a dict: ")
        keys_lists = [x for x in keys]
        key.extend(keys_lists)
        keys_lists.clear()
        values = input("enter the value for a dict: ")
        values_list = [x for x in values]
        value.extend(values_list)
        for key, value in zip(key,value):
            output_of_get = dictionary.get(key, None)
            if output_of_get is None:
                if isinstance(value, list):
                    dictionary[key] = value
                else:
                    dictionary[key] = [value]
            else:
                if isinstance(value, list):
                    dictionary[key].extend(value)
                else:
                    dictionary[key].append(value)
    return dictionary


no_of_dicts = int(input("enter the number of dictionaries: "))
str_to_list_to_dict = str_to_list_to_dict(no_of_dicts)
print(str_to_list_to_dict)


# d = {'a': {1}, 'b': {2}, 'c': {3}}
# c = {'a': {2}, 'b': {3}, 'd': {6}}


def no_of_dictionries_as_input():
    return int(input("enter the no of dictionaries: "))


def output_dict(num):
    dictionries = {}
    for i in range(num):
        keys = []
        values = []
        s = input("enter the keys for a dict: ")
        lists = [x for x in s]
        keys.extend(lists)
        r = input("enter the values for a dict: ")
        list1 = [x for x in r]
        values.extend(list1)
        for k, v in zip(keys, values):
            output_of_get = dictionries.get(k, None)
            if output_of_get is None:
                if isinstance(v, set):
                    dictionries[k] = v
                else:
                    dictionries[k] = {v}
            else:
                if isinstance(v, set):
                    dictionries[k].union(v)
                else:
                    dictionries[k].add(v)
    return dictionries


# num = no_of_dictionries_as_input()
# print(output_dict(num))










