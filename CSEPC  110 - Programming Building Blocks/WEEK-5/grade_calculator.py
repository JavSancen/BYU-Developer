# Asking for a number rate to calculate grade
grade = int(input("What is your rate grade?: "))

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

# Condition to sign
sign = ""
second_digit = grade % 10

if second_digit >= 7:
    sign = "+"
if grade >= 3:
    sign = ""
elif second_digit < 3:
    sign = "-"
elif letter == "F":
    sign = ""
else:
    sign = ""


# Grade condition to pass the class
if grade >= 70:
    print(f'Congratulations you pass the class with "{sign}{letter}"!')
else:
    print(f'Your grade is "{sign}{letter}" Keep trying you can do it the next time.')