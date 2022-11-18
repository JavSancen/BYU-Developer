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
    2. View cart
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
        print("This is your shoping car:")
        print()

        for i in range(len(products)):
            print(f"\n{i} - {products[i]} ${prices[i]}")

    elif choice == "3":
        name_product = input("Name of the article: ")
        if name_product in products:
            index2 = products.index(name_product)
            del products[index2]
            del prices[index2]

            print(f"You delete {name_product}")
        else:
            print("This product doen't exist.")

    elif choice == "4":
        for i in range(len(products)):
            print(f"{i} - {products[i]} ${prices[i]}")
            sum += prices[i]
        print()
        print(f"Total: ${sum}")

    elif choice == "5":
        if input("Are you sure (y/n): ") == "y":
            print("\nThank you, Goodbye.")
            sys.exit()

    else:
        print("\nPlease enter a valid value.")




