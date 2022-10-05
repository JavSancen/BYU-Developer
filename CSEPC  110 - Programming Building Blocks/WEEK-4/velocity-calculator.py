# Team assignment WEEK 4

import math
print("""
Welcome to the velocity calculator.
Please enter the following:
""")
print()

# Inputs for each value
m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Eart, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
r = (A / math.pi) ** 1 / 2
Obj_A = math.pi * (r ** 2)
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# Formulas
import math
c = 1 / 2 * p * Obj_A * C
velocity_t = math.sqrt(m * g / c) * (1 - math.exp((- math.sqrt(m * g * c) / m) * t ))
# Terminal velocity formula
v_terminal = math.sqrt(m * g / c)

# Printing values
print()
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after 10.0 seconds is: {velocity_t:.3f} m/s")
print(f"The terminal velocity is: {v_terminal:.3f} m/s")