import random

attempts = 0
number = random.randint(1, 100)
magic_num = int(input("What is the magic number? "))
number = int(input("What is your guess? "))

while number < magic_num:
    attempts = attempts + 1
    print("Higher")
    number = int(input("What is your guess? "))

while number > magic_num:
    attempts = attempts + 1
    print("Lower")
    number = int(input("What is your guess? "))

print("You guessed it!")
print(f"Your tried {attempts} times")