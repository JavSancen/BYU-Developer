# Asking for the price
child_meal_cost = float(input("What is the price of a child's meal? "))
adult_meal_cost = float(input("What is the price of an adult's meal? "))

# Asking for the number of children's and adult's
children_number = int(input("How many children are there? "))
adults_number = int(input("How many adults are there? "))

tip = float(input("Do you want to add a tip? add the tip rate you wich: "))

# Asking the sales tax rate
tax = float(input("What is the sales tax rate? "))
print()

# Computing and displaying breakdown of amounts
subtotal = (child_meal_cost * children_number) + (adult_meal_cost * adults_number)
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