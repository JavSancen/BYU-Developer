import sys
names = []
prices = []
quantities_sold = []

while True:
    print("Welcome to the Shopping Cart Program!")

    choice = input("""
    Please select one of the following:
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit

    Please enter an action: """)

#products = []
#
#new_product = ""
#new_price = 0
#menu = 0
#total = 0
#
#print("Welcome to the Shopping Cart Program!")
#
#
#
#while menu != "Quit":
#    menu = int(input("""
#    Please select one of the following:
#    1. Add item
#    2. View cart
#    3. Remove item
#    4. Compute total
#    5. Quit
#
#    Please enter an action: """))
#    print()
#
#    if menu == 1:
#        new_product = str(input("Enter a product: "))
#        new_price = (input("Enter a price for this product: "))
#        products.append(f"{new_product} - ${new_price}")
#
#    elif menu == 2:
#        #  elif menu == 2:
#        #print("These are your products")
#        #for i in range(len(products)):
#        #    product = products[i]
#        #    price = prices[i]
#        #    print(f"{product} - {price}")
#        print("This is your list of products")
#        for product in (products):
#            print(product)
#
#    elif menu == 3:
#        products.remove(new_product + " - $" + new_price)
#
#    elif menu == 4:
#        prices = products[1]
#        total = total + prices
#        print(total)
#
#    elif menu == 5:
#        menu = "Quit"
#
#    else:
#        print("Please enter a valid value")
#
#