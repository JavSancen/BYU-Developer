# Example 12

def main():
    gender = input("Enter your gender (M or F): ")

    weight = get_float("Enter your weight in kg: ", 20, 500)
    height = get_float("Enter your height in cm: ", 60, 250)
    age = get_float("Enter your age in years: ", 10, 120)

    bmr = basal_metabolic_rate(gender, weight, height, age)
    print(f"Your basal metabolic rate is {bmr} calories per day.")


def get_float(prompt, lower_bound, upper_bound):
    """Get a number from the user, validate that the user
    entered a number and not some other text, validate that
    the number is between a lower and upper bound, and then
    return the number. If the user enters an invalid number,
    this function will prompt the user repeatedly until the
    user enters a valid number.

    Parameters
        prompt: A string to display to the user.
        lower_bound: The smallest number that the user may enter.
        upper_bound: The largest number that the user may enter.
    Return: The number entered by the user.
    """
    while True:
        try:
            text = input(prompt)
            number = float(text)
            if number < lower_bound:
                print(f"{number} is too small.")
                print("Please enter another number.")
            elif number > upper_bound:
                print(f"{number} is too large.")
                print("Please enter another number.")
            else:
                # If the computer gets to this line of code,
                # the user entered a valid number between
                # lower_bound and upper_bound, so exit the loop.
                break

        except ValueError as val_err:
            # The user entered at least one character that is
            # not part of a floating point number, so print a
            # message asking the user to enter a number.
            print(f"{text} is not a number.")
            print("Please enter a number.")

    return number


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate
    in calories per day. weight must be in kilograms, height
    must be in centimeters, and age must be in years.
    """
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight \
                + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight \
                + 4.799 * height - 5.677 * age
    return bmr


# Call main to start this program.
if __name__ == "__main__":
    main()