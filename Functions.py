def average_marks(marks):
    """calculate the average of marks"""
    sum_of_the_marks = sum(marks)
    total_number_of_subjects = len(marks)
    return sum_of_the_marks / total_number_of_subjects


def compute_garde(average):
    """computing the grade based on the marks obtained"""
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


marks = [56, 78, 98, 89, 0]
average = average_marks(marks)
grade = compute_garde(average)
print(f"The average marks obtained: {average}")
print(f"Grade: {grade}")


# Add and multiply two numbers
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

