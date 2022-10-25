# Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number.

number = 0
intentos = 0

int(input("Enter a number:"))

while number <= 0:
    print("Please enter a positive number")
    intentos = intentos + 1
    number = int(input("Enter a number:"))

print(f"Your number is {number}")
print(f"Your try {intentos} times")

print()

# Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you."

answer = "yes"
answer = str(input("May I have a piece of candy? "))

while answer.lower() != "yes":
    answer = str(input("May I have a piece of candy? "))

print("Thank you!")