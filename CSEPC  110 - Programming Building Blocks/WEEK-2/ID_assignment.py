
# first_name = '[first name]'
# last_name = '[last name],'
# job_title = '[Job title]'
# id_name = 'ID [id number]'
# e_mail= 'email address'
# phone_number = 'phone number'
#
# print('----------------------------------')
# print(last_name.upper(), first_name.capitalize())
# print(job_title)
# print(id_name)
# print()
# print(e_mail)
# print(phone_number)
# print('----------------------------------')



## Second screen
#
#print('Please enter the following information:')
#print()
#first_name = 'Jane'
#last_name = 'Doe,'
#e_mail= 'JaneDoe@email.com'
#phone_number = '(208) 555-1234'
#job_title = 'chief software architect'
#id_name = '83-23821'
#
#
#print('\nThe ID Card is:')
#print('----------------------------------')
#print(last_name.upper(), first_name.capitalize())
#print(job_title)
#print(id_name)
#print()
#print(e_mail)
#print(phone_number)
#print('----------------------------------')



#Final exercice

print('Please enter the following information:')
print()
first_name = input('What is your first name?:' )
last_name = input('What is your last name?:' )
job_title = input('What is your Job title?:' )
id_name = input('What is your ID number?:' )
e_mail= input('What is your email address?:' )
phone_number = input('What is your phone number?:' )
hair = input('What is your hair color?:' )
month = input('What is your month?:' )
eyes = input('What is your eyes color?:' )
training = input('Are you in training?:' )


print('\nThe ID Card is:')
print('----------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(job_title)
print(f'ID: {id_name}')
print()
print(e_mail.lower())
print(phone_number)
print()
print(f"{'Hair: ' + hair:<20} Eyes: {eyes}")
print(f"{'Month: ' + month:<20} Training: {training}")
print('----------------------------------')