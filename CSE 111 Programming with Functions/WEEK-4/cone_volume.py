"""Compute and print the volume of a right circular cone."""

# Import the standard math module so that
# math.pi can be used in this program.
import math


def main():
    # Call the cone_volume function to compute
    # the volume of an example cone.
    # Get the radius and height of the cone from the user.
    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))
    vol = cone_volume(radius, height)
    # Print several lines that describe this program.
    print("This program computes the volume of a right")
    print("circular cone. For example, if the radius of a")
    print(f"cone is {radius} and the height is {height}")
    print(f"then the volume is {vol:.1f}")
    print()

    # Print the radius, height, and
    # volume for the user to see.
    print(f"Radius: {radius}")
    print(f"Height: {height}")
    print(f"Volume: {vol:.1f}")

def cone_volume(radius, height):
    """Compute and return the volume of a right circular cone."""
    volume = math.pi * radius**2 * height / 3
    return volume


# Start this program by
# calling the main function.
main()