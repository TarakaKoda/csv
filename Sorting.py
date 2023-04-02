l1 = [9,3,5,2,7,8,6,1]
# sorted_list = sorted(l1)
# print(sorted_list)
# print(l1)
# l1.sort(reverse=True)
# print(l1)

tup = (9,3,4,5,3,2,4,6)
# print(tup)
tup1 = sorted(tup)
listy = set(tup1)
# print(list(listy))

from operator import attrgetter

l2 = [1,3,4,6,8,2,9,5]
sorted1 = sorted(l2, key=lambda a: a % 2 !=0)
# sorted1 = sorted(l2, key=attrgetter("key")) pass th key name which is present in the dictionary
print(sorted1)

