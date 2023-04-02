person = {"name": "srinu", "age": 25}
sentance = "my name is " + person["name"] + " and i am " + str(person["age"]) + " years old."
# print(sentance)

sentance1 = "my name is {} and i am {} years".format(person["name"], person["age"])
# print(sentance1)

sentance2 = "my name is {0} and i am {0} years old".format(person["name"], person["age"])
# print(sentance2)

tag, text = "h1", "this is a headline"
sentance3 = "<{0}>{1}</{0}>".format(tag, text)
# print(sentance3)

sentance4 = "my name is {0[name]} and i am {1[age]} years old".format(person, person)
# print(sentance4)

sentance5 = "my name is {0[name]} and i am {0[age]} years old".format(person)
# print(sentance5)

list1 = ["srinu", 25]
sentance6 = "my name is {0[0]} and i am {0[1]} years old".format(list1)
# print(sentance6)

class Person():
    def __init__(self, name,age):
        self.name = name
        self.age = age

p1 = Person("srinu", 25)
# print("my name is {0.name} and i am {0.age} years old".format(p1))

sentance7 = "my name is {name} and my age is {age}".format(name= "srinu", age= 25)
# print(sentance7)

person1 = {"name": "srinivas", "age": 25}
b, c = person1.values()
# print(c)
# print(b)
sentance8 = "my name is {name} and i am {age} yeas old".format(**person1)
# print(sentance8)


# for i in range(1,11):
#     print("The value of i is {:03}".format(i))

pi = 3.14159265

sentance9 = "Pi is equal to {:.2f}".format(pi)
# print(sentance9)

sentance10 = "1 MB is equals to {:,.2f} bytes".format(1000**2)
# print(sentance10)

# Formatting Dates
from datetime import datetime
my_datetime = datetime(2023, 3, 29, 7, 30, 35)
# print(my_datetime)

sentance11 = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year {0:%Y}".format(my_datetime)
# print(sentance11)


list1 = frozenset("python")
# print(list1)
list2 = frozenset("python")
# print(list2)
print(list1 == list2, list1 is list2)














