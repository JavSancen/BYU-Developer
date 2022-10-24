# Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number. For example:

number = 0

int(input("Enter a number:"))

while number <= 0:
    print("Please enter a positive number")
    number = int(input("Enter a number:"))

print(f"Your number is {number}")

print()

# Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you." For example:
answer = "yes"
answer = str(input("May I have a piece of candy? "))

while answer.lower() != "yes":
    answer = str(input("May I have a piece of candy? "))

print("Thank you!")