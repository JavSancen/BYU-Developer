first_name = input('What is your first name?: ')
last_name = input('What is your last name?: ')

# james_bound_name = 'Your name is ' + last_name + ', ' + first_name + ' ' + last_name
# james_bound_name = 'Your name is {}, {} {}' .format(last_name, first_name, last_name)
# james_bound_name = 'Your name is {1}, {0} {1}' .format(first_name, last_name)
james_bound_name = f'Your name is {last_name}, {first_name} {last_name}'
print(james_bound_name)