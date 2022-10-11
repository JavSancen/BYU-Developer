print("""
---------------------------------
Menu

Hamburguer Child Package - $5.99
Hamburguer Adult Package - $7.99

Child Drink - $3.50
Adult Drink - $5.99
---------------------------------
""")

# Asking for the number of each package and drinks
child_hamburguer = float(input("How many Hamburguer Child Packages do you want? "))
adult_hamburguer = float(input("How many Hamburguer Adult Packages do you want? "))
child_drink = float(input("How many Child Drinks do you want? "))
adult_drink = float(input("How many Adult Drink do you want? "))

# Computing order calculation
children_order= (child_hamburguer * 5.99) + (child_drink * 3.50)
adults_order = (adult_hamburguer * 7.99) + (adult_drink * 5.99)

tip = float(input("Do you want to add a tip? add the tip rate you wich: "))

# Asking the sales tax rate
tax = float(16)
print()

# Computing and displaying breakdown of amounts
subtotal = children_order + adults_order
tip_rate = subtotal * (tip / 100)
sales_tax = subtotal * (tax / 100)
total = subtotal + sales_tax
including_tip = total + tip_rate
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tip: ${tip_rate:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
# Adding the tip rate
print(f"Including Tip: ${including_tip:.2f}")
print()

# Computing payment amount and change
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
change_including_tip = payment_amount - including_tip
print(f"Change: ${change:.2f}")
print()
print("Do you want add the tip?")
print("Yes.")
print()
print(f"Change: ${change_including_tip:.2f}")

"""
I used fixed values to the menu as in a restaurant.
The tax rate value is a fix value I'm based in the tax rate here in Mexico for IVA
I did in this way to simplify and reduce the information user need to update
It is a very simple example but it is like thinking in a real restaurant.
And I also print only two float numbers to the values.

At the end I show the change with and without tip change with a short real conversation example
"""
