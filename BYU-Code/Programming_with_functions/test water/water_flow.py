"""
    Author:  Group 2

    Class:  CSE111-23s-a3

    Instructor:  Brother Curtis Nelson

    Date:  05/27/2023

    Version:  1.0

"""

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
EARTH_GRAVITY = 9.80665              # (meters / second2)
WATER_DENSITY = 998.2                # (kilogram / meter3)
WATER_DYNAMIC_VISCOSITY = 0.0010016  # (Pascal seconds)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    pound_square =  kilopascal_to_pound_square_inch(loss)

    print(f"Pressure at house: {pressure:.1f} kilopascals")

def water_column_height(tower_height, tank_height):
    water_height = tower_height + ( 3 * tank_height) / 4
    return water_height

def pressure_gain_from_water_height(water_column_height):
    pressure = WATER_DENSITY * EARTH_GRAVITY * water_column_height / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    pressure_loss_from_pipe = ( friction_factor*(-1)) * pipe_length * WATER_DENSITY * fluid_velocity** 2 / (2000 * pipe_diameter)
    return pressure_loss_from_pipe

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    loss = -0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings / 2000
    return loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    reynolds = WATER_DENSITY * hydraulic_diameter * fluid_velocity / 0.0010016
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    constant = (0.1 + (50 / reynolds_number)) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    loss = (constant*(-1)) * WATER_DENSITY * fluid_velocity ** 2 / 2000
    return loss

def kilopascal_to_pound_square_inch(loss):
    pound_square = loss * 0.145038
    return pound_square

if __name__ == "__main__":
    main()