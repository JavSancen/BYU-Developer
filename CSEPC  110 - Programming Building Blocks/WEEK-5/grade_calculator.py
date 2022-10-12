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

# Grade condition to pass the class
if grade >= 70:
    print(f'Congratulations you pass the class with "{letter}"!')
else:
    print(f'Your grade is "{letter}" Keep trying you can do it the next time.')