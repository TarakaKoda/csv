courses = ["History", "Science", "Mathematics", "CompSci"]
# # print(courses)
# # print(len(courses))
# # print((courses[1][-3::-2]))
#
# courses.append("civics")
# print(courses)
#
courses.extend(["social", "math"])
# print(courses)

courses[-1:-1] = ["chem", "sat"]
# print(courses)

#
# courses.insert(1,"hindi")
# print(courses)
#
# courses.remove("hindi")
# print(courses)
#
# courses.pop(2)
# print(courses)
#
# q = courses.copy()
# print(q)
#
# q.clear()
# print(q)
#
# print(courses.count("History"))
# print(courses.index("History"))
#
courses.reverse()
# print(courses)
# courses.sort(reverse=False)
# print(courses)
#
# sorted(courses)
# print(courses)
#
# # Adding items using slicing.
# courses[1:1] = ["hindi", "english"]
# print(courses)
#
# courses[3:4] = ["good", "bad"]
# print(courses)

number = [1, 2, 5, 4, 3, 5, 9, 2]
# sorted_list = []
# while number:
#     sorted_list.append(max(number))
#     number.remove(max(number))
# print(sorted_list)
# print(len(sorted_list)

# Sorting a list using a for loop.
for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]
# print(number)

for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]
number.sort(reverse=True)
q = number.copy()
# print(q)
number.sort()
# print(number)
# print(q)

# num = input("enter the range of number: ")
# a, b = 0, 1
# for i in range(int(num)):
#     # print(b)
#     a, b = b, a+b

courses = ["history", "math", "hindi", "social"]
courses2 = ["art", "education"]
# courses2.insert(1, courses)
# print(courses2)
# course = []
# j = len(courses)-1
# while j >= 0:
#     course.append(courses[j])
#     j -= 1
# # print(course)
#
# for index, value in enumerate(courses):
#     print(index, value)
num = "11277399388r4934772893"
clean_num = " ".join(set(num))
list = sorted(clean_num)
result = " ".join(list)
# print(result.strip())
# print(help(list))

nums = [1,2,3,4,5,6,7,8,9]

# I want 'n' for each 'n' in nums
# mylist = []
# for n in nums:
#     mylist.append(n)
# print(mylist)
# using list comprehension
# mylist = [n for n in nums]
# print(mylist)

# I want 'n*n' for each 'n' in nums
# mylist = []
# for n in nums:
#     mylist.append(n*n)
# print(mylist)
# using the list comprehension
# mylist = [n*n for n in nums]
# print(mylist)

# I want 'n' for each 'n' in nums if 'n' is even.
# mylist = []
# for n in nums:
#     if n%2 == 0:
#         mylist.append(n)
# print(mylist)
# mylist = [n for n in nums if n % 2 == 0]
# print(mylist)

numbers = [1,3,5,6,7,8,3]
mylist = [(i,j) for i in range(len(numbers)) for j in range(i+1, len(numbers)) if numbers[i] > numbers[j]]
# print(mylist)


def average_marks(marks):
    sum_of_the_marks = sum(marks)
    total_number_of_subjects = len(marks)
    return sum_of_the_marks / total_number_of_subjects


def compute_garde(average):
    if 80 <= average <= 100:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 50:
        grade = 'D'
    else:
        grade = 'F'
    return grade


marks = [56, 78, 98, 87, 90]
average = average_marks(marks)
grade = compute_garde(average)
print(f"The average marks obtained: {average}")
print(f"Grade: {grade}")


def add_number(a,b):
    addition = a + b
    return addition


def multiply_number(a,b):
    multiplication = a * b
    return multiplication


add = add_number(2,6)
multiply = multiply_number(2, 6)
print(f"Addition of two numbers: {add}")
print(f"Multiplication of two numbers: {multiply}")


