# I found this sys module in Python witch provides various
# functions and variables that are used to manipulate different
# parts of the Python runtime environment.
import sys
products = []
prices = []

product = ""
price = 0
sum = 0

print("Welcome to the Shopping Cart Program!")

while product != "quit":

    choice = input("""
    Please select one of the following:
    1. Add item
    2. View shopping cart
    3. Remove item
    4. Compute total
    5. Quit

    Please enter an action: """)

    if choice == "1":
        product = input("What is the name of your product?: ")
        price = float(input("What is the price of your product?: "))
        products.append(product)
        prices.append(price)

    elif choice == "2":
        print()
        print("This is your shopping cart:")
        print()

        for i in range(len(products)):
            print(f"\n{i} - {products[i]} ${prices[i]}")

# I tried to simplify the way to delete a product calling the product I want to delete
# With an index, in this way you just need to write the name of the product you
# want to delete.
    elif choice == "3":
        name_product = input("Name of the product to delete: ")
        if name_product in products:
            index2 = products.index(name_product)
            del products[index2]
            del prices[index2]

            print(f"You delete {name_product}")
        else:
            print("This product doesn't exist.")

    elif choice == "4":
        for i in range(len(products)):
            print(f"{i} - {products[i]} ${prices[i]}")
            sum += prices[i]
        print()
        print(f"Total: ${sum}")

# I used the sys module here to confirm if the user wants to close the program.
    elif choice == "5":
        if input("Are you sure (y/n): ") == "y":
            print("\nThank you, Goodbye.")
            sys.exit()

# This section guide user to know if the entry is correct
    else:
        print("\nPlease enter a valid value.")




