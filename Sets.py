sets = ['history', 'maths', 'physics']
# print('history' in sets)
sets1 = set(sets)
# print(type(sets1))
set2 = {'history', 'maths', 'social', 'art'}
result = sets1.union(set2)
# print(sorted(result))
# print(sorted(sets1.intersection(set2)))
# print(sorted(sets1.difference(set2)))
# print(sets1)
# print(help(set))
a = {1,2,3,4,5}
b = {2,3,4,5,6}
# print(a.difference_update(b))
# print(a)


d = {'a': {1}, 'b': {2}, 'c': {3}}
c = {'a': {2}, 'b': {3}, 'd': {6}}


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


num = no_of_dictionries_as_input()
print(output_dict(num))

