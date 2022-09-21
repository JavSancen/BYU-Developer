verb = input('What is something you like to do? ')
print('When I have free time, I really enjoy {}'.format(verb.lower()))

first_name = 'Francisco'
last_name = 'Zúñiga'

# output = 'Hello, ' + first_name + ' ' + last_name
# output = 'Hello, {} {}' .format(first_name, last_name)
# output = 'Hello, {1}, {0}' .format(first_name, last_name)
output = f'Hello, {first_name} {last_name}'
print(output)