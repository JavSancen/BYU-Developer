#import math
#
#def area_square(side):
#    square = side * side
#    return square
#
#def area_rectangle(side, base):
#    rectangle = side * base
#    return rectangle
#
#def area_circle(radious):
#    circle = math.pi*radious**2
#    return circle
#
#shape = None
#while shape != quit:
#    shape = input("""What kind of shape do you have?
#    - square
#    - rectangle
#    - circle
#
#choice one:
#    """)
#
#    if shape == 'square':
#        value = float(input("What is es the value of the side of the square?: "))
#        print(f"The area of the square is {area_square(value)}")
#
#    elif shape == 'rectangle':
#        value = float(input("What is es the value of the side of the rectangle?: "))
#        value2 = float(input("What is es the value of the base of the rectangle?: "))
#        print(f"The area of the rectangle is {area_rectangle(value, value2)}")
#
#    elif shape == 'circle':
#        value = float(input("What is es the value of the radius of the circle?: "))
#        print(f"The area of the circle is {area_circle(value)}")
#
#

import math

def area_square(side):
    area = area_rectangle(side, side)
    return area

def area_rectangle(side, base):
    return side * base

def area_circle(radious):
    return math.pi*radious**2

def area_value(shape, side1, side2=0):
    area = -1

    if shape == 'square':
        area = area_square(side1)
    elif shape == 'rectangle':
        area = area_rectangle(side1, side2)
    elif shape == 'circle':
        area = area_circle(side1)

    return area


shape = None
while shape != quit:
    shape = input("""What kind of shape do you have?
    - square
    - rectangle
    - circle

choice one:
    """)

    if shape == 'square':
        value = float(input("What is es the value of the side of the square?: "))
        area = area_value(shape, value)
        print(f"The area of the square is {area:.2f}")

    elif shape == 'rectangle':
        value = float(input("What is es the value of the side of the rectangle?: "))
        value2 = float(input("What is es the value of the base of the rectangle?: "))
        area = area_value(shape, value, value2)
        print(f"The area of the rectangle is {area:.2f}")

    elif shape == 'circle':
        value = float(input("What is es the value of the radius of the circle?: "))
        area = area_value(shape, value)
        print(f"The area of the circle is {area:.2f}")
