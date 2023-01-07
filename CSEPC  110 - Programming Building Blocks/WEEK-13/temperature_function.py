
def F_t(T, V):
    F = 35.74 + 0.6215*T - 35.75 *V**0.16 + 0.4275*T*V**0.16
    return F

# I convert °F to °C
def C_t(T, V):
    C = 35.74 + 0.6215*T - 35.75 *V**0.16 + 0.4275*T*V**0.16 - 32 / 1.8000
    return C

option = None
while option != quit:
    option = input("""Fahrenheit or Celsius (F/C)? """)

    if option == 'F':
        value = int(input("What is the temperature?  "))
        value2 = int(input("Enter a value for the wind speed: "))
        print(f"At temperature {value} °F, and wind speed {value2} mph, the windchill is: {F_t(value, value2):.4f} °F")

    elif option == 'C':
        value = int(input("What is the temperature?  "))
        value2 = int(input("Enter a value for the wind speed: "))
        print(f"At temperature {value} °C, and wind speed {value2} mph, the windchill is: {C_t(value, value2):.4f} °C ")

    else:
        print("Enter a valid value")

