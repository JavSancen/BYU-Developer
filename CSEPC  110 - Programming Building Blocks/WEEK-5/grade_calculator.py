# Asking for a number rate to calculate grade
grade = int(input("What is your rate grade?: "))
sign = ""
second_digit = grade % 10

if grade >= 90:
    letter = 'A'
if grade >= 80:
    letter = 'B'
if grade >= 70:
    letter = 'C'
if grade >= 60:
    letter = 'D'
else:
    letter = 'F'

if second_digit >= 7:
    sign = "+"
elif second_digit < 3:
    sign = "-"
else:
    sign = ""

if grade >= 93:
    sign = ""

if letter == "F":
    sign = ""

# Grade condition to pass the class
if grade >= 70:
    print(f'Congratulations you pass the class with "{sign}{letter}"!')
else:
    print(f'Your grade is "{letter}" Keep trying you can do it the next time.')