# Asking for the price
child_meal_cost = float(input("What is the price of a child's meal? "))
adult_meal_cost = float(input("What is the price of an adult's meal? "))

# Asking for the number of children's and adult's
children_number = float(input("How many children are there? "))
adults_number = float(input("How many adults are there? "))

# Asking the sales tax rate
tax = float(input("What is the sales tax rate? "))
print()

# Computing and displaying breakdown of amounts
subtotal = (child_meal_cost * children_number) + (adult_meal_cost * adults_number)
sales_tax = subtotal * (tax / 100)
total = subtotal + sales_tax
print(f"Subtotal: ${subtotal}")
print(f"Sales Tax: ${sales_tax}")
print(f"Total: ${total}")
print()

# Computing payment amount and change
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print(f"Change: {change}")