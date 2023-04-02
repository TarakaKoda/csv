# Check if the list contains integer x
l = [x for x in range(10)]
# print(2 in l)


# Find duplicate number in integer list
def duplicate_num(l):
    duplicate = set()
    seen = set()
    for i in l:
        if i not in duplicate:
            duplicate.add(i)
        else:
            seen.add(i)
    return list(duplicate)


list1 = [x for x in range(10)]
list1[1:1] = [x for x in range(10)]
# print(duplicate_num(list1))

# Check if two string is anagram
def anagram(s1,s2):
    return set(s1) == set(s2)


# print(anagram("srinu","unirs"))

# Remove all duplicates from a list
l2 = [x for x in range(10)] + [x for x in range(10)]
# print(list(set(l2)))

# Sorting a list using a for loop
l3 = [55,333,44,5,37,999]
for i in range(len(l3)):
    for j in range(i+1, len(l3)):
        if l3[i] > l3[j]:
            l3[i],l3[j] = l3[j], l3[i]
# print(l3)


# finding the miss match terms in a string
string1 = sorted("aassddffgghjjkkll")
string2 = "aassddffgghhjlkll"
zip_seqs = zip(string1, string2)
# print(list(zip_seqs))
enum_seqs = enumerate(zip_seqs)
# for i, (k,v) in enum_seqs:
#     if k != v:
#         print(f"index: {i} value: {k,v}")
#         print(i)
# print(string1)
# print(string2)
a: str = "srinu"
n: int = 123

for i in range(len(string1)):
    for j in range(i+1 , len(string1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
string = "".join(string1)
# print(string)


def duplicate_list():
    return [x for x in range(10)] + [x for x in range(10)]


def remove_duplicates(dlist):
    seen, duplicate = set(), set()
    for i in dlist:
        if i in seen:
            duplicate.add(i)
        seen.add(i)
    return duplicate


dlist = duplicate_list()
rduplicates = remove_duplicates(dlist)
# print(sorted(rduplicates))
# set1 = {"srinu", "pavan","sai","laku"}
# print(sorted(set1))



def find_pair(x,n):
    pair =[]
    list2 = [x for x in range(n)]
    for i in list2:
        for j in list2[i+1:]:
            if list2[i] + list2[j] == x:
                pair.append((list2[i],list2[j]))
    return {x for x in pair}


result = find_pair(9,10)
# print(result)
# def pair(x):
#     pair2 = set()
#     list3 = [x for x in range(10)]
#     for i,enum1 in enumerate(list3):
#         for j,enum2 in enumerate(list3[i+1:]):
#             if enum1 + enum2 == x:
#                 pair2.add((enum1,enum2))
#
#
#     return sorted(list(pair2))

#print(pair(9)

list1 = [[x,y] for x in range(10) if x%2==0 and x!=0 for y in range(10) if y%2 !=0]
# print(sorted(list1))
list4 = list(map(lambda x:x.pop(), list1))
list5 = list(map(lambda y: y.pop(0),list1))
list5_remove = sorted(set(list5))
list4_remove = sorted(set(list4))
# print((list4_remove)+ list(list5_remove))
# print(help(set))


def factorial(n: int) -> int:
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def missing_number(list):
    return set(range(len(list)-1)[1:]) - set(list)


list = list(range(1,100))
list.remove(55)
result = missing_number(list)
print((result))

