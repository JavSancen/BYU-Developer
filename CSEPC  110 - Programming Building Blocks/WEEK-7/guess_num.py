from random import random


import random

magic_number = random.randint(1,10)
ask = "yes"

while ask == "yes":
    guess_num = -1
    attempts = 0

    while guess_num != magic_number:
        guess_num = int(input("What is your guess? "))
        attempts += 1
        if guess_num > magic_number:
            print("Lower")

        elif guess_num < magic_number:
            print("Higher")

        else:
            print("You guess it!")

    print(f"You try {attempts} times")

    ask = str(input("Do you want to play again?"))

