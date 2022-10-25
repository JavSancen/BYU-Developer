
print("Welcome to the word guessing game!")
print()

attempts = 0

#Have a secret word stored in the program.
secret_word = str(input("What is the secret word? "))
#Prompt the user for a guess.
guess = str(input("What is your guess? "))

#Continue looping as long as that guess is not correct.
while guess.lower() != secret_word.lower():
    #Calculate the number of guesses and display it at the end.
    attempts = attempts + 1
    print("Your guess was not correct.")
    guess = str(input("What is your guess?: "))

print("Congratulations! You guessed it!")
print(f"Your tried {attempts} times")