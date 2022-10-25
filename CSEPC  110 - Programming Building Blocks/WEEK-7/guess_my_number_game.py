import random

number = random.randint(1, 100)
magic_num = int(input("What is the magic number? "))
number = int(input("What is your guess? "))

while number < magic_num:
    print("Higher")
    number = int(input("What is your guess? "))

while number > magic_num:
    print("Lower")
    number = int(input("What is your guess? "))

print("You guessed it!")