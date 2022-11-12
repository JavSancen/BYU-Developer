numbers = []

count = 0
sum = 0
new_number = -1

print("Enter a list of numbers, type 0 when you finish.")
while new_number != 0:
    new_number = int(input("Enter number: "))

    if new_number != 0:
        numbers.append(new_number)

max = numbers[0]
min_positive = numbers [0]

for number in numbers:
    sum += number
    count += 1
    if number > max:
        max = number
    elif number < min_positive and number > 0:
        min_positive = number

print()
print(f"The sum is: {sum} ")
print(f"The average is: {sum/count} ")
print(f"The largest number is: {max} ")
print(f"The smallest number is: {min_positive} ")
print()
print(f"The sorted list is: ")

for sorted_numbers in sorted(numbers):
    print(sorted_numbers)
