people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

max_age = -1
min_age = +1
max_name = "" # It doesn't matter what you set this to, it just needs to be declared
min_name = ""

for item in people:

    part = item.split(" ")
    people_name = str(part[0]) # name is the first part
    age = int(part[1])

    if age > max_age:
        # This is the new max
        max_age = age

        # Also save this product name as the max name
        max_people = people_name
    elif age < max_age and age < 10:
        min_age = age
        min_people = people_name

print(f"The maximum age is: {max_age}")
print(f"The person with the maximum age is: {max_people}")
print(f"The maximum age is: {min_age}")
print(f"The person with the minimum age is: {min_people}")