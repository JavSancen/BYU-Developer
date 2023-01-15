"""

    Author:  Team 5

    Class:  111-15

    Instructor:  Brother Christian Eisinger

    Date:  1/14/2023

    Version:  1.0



    Problem Statement:

        Health professionals who are helping a client achieve a healthy body weight,

sometimes use two computed measures named body mass index and basal metabolic rate.

        From the U.S. Centers for Disease Control and Prevention we read, Body mass index

(BMI) is a person’s weight in kilograms divided by the square of their height in meters.

BMI can be used to screen for weight categories such as underweight, normal, overweight,

and obese that may lead to health problems. However, BMI is not diagnostic of the body

fatness or health of an individual.

        The formula for computing BMI is

            bmi = 10,000 * weight / height ^ 2

where weight is in kilograms and height is in centimeters.

        Basal metabolic rate (BMR) is the minimum number of calories required daily to

keep your body functioning at rest. BMR is different for women and men and changes with

age. The revised Harris-Benedict formulas for computing BMR are

    (women)  bmr = 447.593 + 9.247 weight + 3.098 height - 4.330 age

    (men)  bmr = 88.362 + 13.397 weight + 4.799 height - 5.677 age

where weight is in kilograms and height is in centimeters.




    Assignment:

        Work as a team to write a Python program named fitness.py that does the following:

            Asks the user to enter four values:

                gender

                birthdate in this format: YYYY-MM-DD

                weight in U.S. pounds

                height in U.S. inches

            Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).

            Converts inches to centimeters (1 in = 2.54 cm).

            Calculates age, BMI, and BMR.

            Prints age, weight in kg, height in cm, BMI, and BMR.




    Stretch Challenges:

        If your team finishes the core requirements in less than an hour, complete one or

more of these stretch challenges. Note that the stretch challenges are optional.

        * Modify your program to print the height values in meters instead of centimeters.

        * Modify your program to allow the user to enter weight in British stones and add

a function named kg_from_stone.

        * Modify your program to allow the user to enter height as U.S. feet and inches.

        * Add something or change something in your program that you think would make your

program better, easier for the user, more elegant, or more fun. Be creative.

"""

# Import datetime so that it can be

# used to compute a person's age.

from datetime import datetime




def main():

    # Get the user's gender, birthdate, height, and weight.

    gender = ''

    while gender not in ['m', 'f', 'male', 'female']:

        gender = input('Enter your gender ex(M/F):  ').lower()

    if gender == 'male':  gender = 'm'

    elif gender == 'female':  gender = 'f'

    age = -1

    while age < 0:

        birthdate = input('Enter your birthday (YYYY-MM-DD):  ')

        age = compute_age(birthdate)

    weight = float(input('Enter your weight in U.S. Pounds ex(150.0):  '))

    height = float(input('Enter your height in U.S. Inches ex(70.0):  '))


 

    # Call the compute_age, kg_from_lb, cm_from_in,

    # body_mass_index, and basal_metabolic_rate functions

    # as needed.

    kg = kg_from_lb(weight)

    cm = cm_from_in(height)

    bmi = body_mass_index(kg, cm)

    bmr = basal_metabolic_rate(gender, kg, cm, age)


 

    # Print the results for the user to see.

    print(f'Age (years): {age:.0f}')

    print(f'Weight (kg): {kg:.2f}')

    print(f'Height (cm): {cm:.1f}')

    print(f'Body mass index: {bmi:.1f}')

    print(f'Basal metabolic rate (kcal/day): {bmr:.0f}')



 

def compute_age(birth_str):

    """Compute and return a person's age in years.

    Parameter birth_str: a person's birthdate stored

        as a string in this format: YYYY-MM-DD

    Return: a person's age in years.

    """

    # Convert a person's birthdate from a string

    # to a date object.

    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")

    today = datetime.now()



    # Compute the difference between today and the

    # person's birthdate in years.

    years = today.year - birthdate.year




    # If necessary, subtract one from the difference.

    if birthdate.month > today.month or \
        (birthdate.month == today.month and \

            birthdate.day > today.day):

        years -= 1



    return years



 

def kg_from_lb(pounds):

    """Convert a mass in pounds to kilograms.

    (1 lb = 0.45359237 kg)

    Parameter pounds: a mass in U.S. pounds.

    Return: the mass in kilograms.

    """

    return pounds * 0.45359237




def cm_from_in(inches):

    """Convert a length in inches to centimeters.

    (1 in = 2.54 cm)

    Parameter inches: a length in inches.

    Return: the length in centimeters.

    """

    return inches * 2.54



def body_mass_index(weight, height):

    """Compute and return a person's body mass index.

    bmi = 10,000 * weight / height ^ 2

    Parameters

        weight: a person's weight in kilograms.

        height: a person's height in centimeters.

    Return: a person's body mass index.

    """

    return 10000 * weight / height ** 2



 

def basal_metabolic_rate(gender, weight, height, age):

    """Compute and return a person's basal metabolic rate.

    (women)  bmr = 447.593 + 9.247 weight + 3.098 height - 4.330 age

    (men)  bmr = 88.362 + 13.397 weight + 4.799 height - 5.677 age

    Parameters

        weight: a person's weight in kilograms.

        height: a person's height in centimeters.

        age: a person's age in years.

    Return: a person's basal metabolic rate in kcals per day.

    """

    constants = {

        'm' : [88.362, 13.397, 4.799, - 5.677],

        'f' : [447.593, 9.247, 3.098, - 4.330]

    }

    return constants[gender][0] + constants[gender][1] * weight + constants[gender][2] * height + constants[gender][3] * age



 

# Call the main function so that

# this program will start executing.

main()