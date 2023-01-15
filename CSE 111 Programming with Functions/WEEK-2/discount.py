from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()


subtotal = float(input("Please enter the subtotal: "))

if day_of_week == 1 and subtotal > 50:
    discount = subtotal * .1
    taxes = (subtotal - discount) * 0.06
    subtotal = subtotal - discount
    with_taxes = taxes + subtotal
    print(f"Discount amount: {discount:.2f}")

elif day_of_week == 2 and subtotal > 50:
    discount = subtotal * .1
    taxes = (subtotal - discount) * 0.06
    subtotal = subtotal - discount
    with_taxes = taxes + subtotal
    print(f"Discount amount: {discount:.2f}")

else:
    taxes = subtotal * 0.06
    with_taxes = taxes + subtotal

print(f"Sales tax amount: {taxes:.2f}")
print(f"Total: {with_taxes:.2f}")
