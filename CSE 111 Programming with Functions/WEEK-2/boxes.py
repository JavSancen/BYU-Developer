import math

t_items = int(input("Enter the number of items: "))
n_items = int(input("Enter the number of items per box: "))
calc_boxes = t_items / n_items
req_boxes = math.ceil(calc_boxes)
print()
print(f"For {t_items} items, packing {n_items} items in each box, you will need {req_boxes} boxes.")