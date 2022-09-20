# WEEK-2 NOTEs

To place name for our variables we have two options

```
# We can't use spaces for long names
this_is_a_long_name_for_a_variable

# We can also use the camel case option wich is used in other lenguages like javascript too
thisIsaLongNameForaVariable
```

To place notes in our code we can use this method:

```
# This is only a comment and do nothing in your code.
# It helps to document code and make it easy to understand to others
# Also it helps to try cases to debug
```

How to use strings?

```
sentence = 'The dogs name is Hopper'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

# /bin/python3 "/home/francisco/BYU/BYU-Developer/CSEPC  110 - Programming Building Blocks/WEEK-2/strings.py"
# THE DOGS NAME IS HOPPER
# the dogs name is hopper
# The dogs name is hopper

first_name = input('What is your first name?: ')
last_name = input('What is your last name?: ')
print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())

# What is your first name?: FRANCISCO
# What is your last name?: ZUÑIGA
# Hello Francisco Zuñiga
```

Code  | Result
---------------------------- | ---------------------
words = "the cat IN THE hat"  | the cat IN THE hat
words.capitalize()  | The cat in the hat
words.title()  |  The Cat In The Hat
words.upper()  |  THE CAT IN THE HAT
words.lower()  |  the cat in the hat
words.count("t")  |  3
words.lower().count("t")  |  4









