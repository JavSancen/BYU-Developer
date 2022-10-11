# Asking number values
first_num = int(input("What is the first number?: "))
second_num = int(input("What is the second number?: "))

# Conditions for number values
if first_num > second_num:
    print(f"The first number {first_num} is greater")
    if first_num != second_num:
        print(f"The numbers are not equals")
    if second_num < first_num:
        print(f"The second number {second_num} is not greater")
    else:
        print("Enter a number")

print()

# Asking for a favorite animal
fav_animal = input("What is your favorite animal?: ")

# Condition for favorite animal
if fav_animal.upper() == "BEAR":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
