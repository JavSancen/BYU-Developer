# Asking for a number rate to calculate grade
grade = int(input("What is your rate grade?: "))

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

# Condition to sign
sign = ""
second_digit = grade % 10

if second_digit >= 7:
    sign = "+"
elif grade >= 3:
    sign = ""
if second_digit < 3:
    sign = "-"

# Setting only F in the case between 59 and 0
if letter == "F":
    sign = ""


# Grade condition to pass the class
if grade >= 70:
    print(f'Congratulations you pass the class with "{sign}{letter}"!')
else:
    print(f'Your grade is "{sign}{letter}" Keep trying you can do it the next time.')