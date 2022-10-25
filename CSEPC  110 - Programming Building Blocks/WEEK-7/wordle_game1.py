from mimetypes import guess_all_extensions


print("Welcome to the word guessing game!")
print()

secret_word = ""
secret_word = str(input("What is your secret word?: "))

while secret_word == guess:
    guess = str(input("What is your guess?: "))
    print("Your guess was not correct.")

print("Congratulations! You guessed it!")