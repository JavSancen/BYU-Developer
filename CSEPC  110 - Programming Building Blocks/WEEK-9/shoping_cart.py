products = []
prices = []

new_product = ""
new_price = 0
sum = 0
menu = 0

print("Welcome to the Shopping Cart Program!")



while menu != "Quit":
    menu = int(input("""
    Please select one of the following:
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit
    Please enter an action: """))

    if menu == 1:
        item = products + str(new_price)
        new_product = str(input("Enter a product: "))
        new_price = int(input("Enter a price for this product"))
        products.append(new_product)
        prices.append(new_price)

    elif menu == 2:
        print("These are your products")
        for product in products and price in prices:
            print(f"{product}  ${prices}")





