age = input('How old are you? ')
future_age = int(age) + 1

print('On your next birtday, you will be ' + str(future_age))

print()

egg_cartons = input('How many egg cartons do you have? ')
eggs = int(egg_cartons) * 12

print('You have ' + str(eggs))

print()

cookies = input('How many cookies do you have? ')
people = input('How many people are there? ')
portion = float(cookies) / float(people)

print('Each person may have ' + str(portion) + ' cookies')