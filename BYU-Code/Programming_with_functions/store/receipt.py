"""
    Author:  Francisco Javier Zúñiga Sancén

    Class:  CSE111-23s-a3

    Instructor:  Brother Curtis Nelson

    Date:  06/24/2023

    Version:  1.0

"""

import csv

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
discount_day = current_date_and_time.weekday()
#discount_time =
#print(current_date_and_time)
#print(discount_day)

#discount_date = datetime.weekday(0)
#print(discount_date)

print("\nCornel Store")
print()

def main():
    # Index of the dictionary and list column
    # in the products.csv and request.csv files.
    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    REQUEST_INDEX = 0
    QUANTITY_INDEX = 1

    subtotal_bill = 0
    num_items = 0
    discount = 0

    # Read the contents of the products.csv into a
    # compound dictionary named products_dict. Use
    # the product code as the keys in the dictionary.
    products_dict = read_dictionary("products.csv", PRODUCT_INDEX)

    # Print the products compound dictionary.
    #print(products_dict)
    req_list = []
    with open('request.csv', 'rt') as file:
        reader = csv.reader(file)
        next(reader)

        for row_list in reader:
            req_list = row_list

            if len(row_list) != 0:
                req_id = req_list[REQUEST_INDEX]
                quantity = int(req_list[QUANTITY_INDEX])
                value = products_dict[req_id]
                name = value[NAME_INDEX]
                price = float(value[PRICE_INDEX])
                total_price = price * quantity
                subtotal_bill += total_price
                num_items += quantity
                tax = subtotal_bill * .06
                total = subtotal_bill + tax - discount
                print(f"{name} -- {quantity} --- ${total_price}")

        print(f"\nNumber of items {num_items}")
        print(f"Subtotal: ${subtotal_bill:.2f}")
        print(f"Sales Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")

        print()
        if discount_day == 5:
        #if discount_day == 1 or discount_day == 2:
            discount = subtotal_bill * 0.1
            total_with_discount = subtotal_bill + tax - discount
            print(f"Today is {current_date_and_time:%A} you have a discount of 10% in your bill before taxes")
            print(f"Total with discount: ${total_with_discount:.2f}")

        print("\nThank you for shopping at the Cornel Store.")
        print(f"{current_date_and_time:%A %I:%M %p}")
        print()


def read_dictionary(filename, key_column_index):
    try:
        """Read the contents of a CSV file into a compound
        dictionary and return the dictionary.

        Parameters
            filename: the name of the CSV file to read.
            key_column_index: the index of the column
                to use as the keys in the dictionary.
        Return: a compound dictionary that contains
            the contents of the CSV file.
        """
        # Create an empty dictionary that will
        # store the data from the CSV file.
        dictionary = {}

        # Open the CSV file for reading and store a reference
        # to the opened file in a variable named csv_file.
        with open(filename, "rt") as csv_file:

            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(csv_file)

            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(reader)

            # Read the rows in the CSV file one row at a time.
            # The reader object returns each row as a list.
            for row_list in reader:

                # If the current row is not blank, add the
                # data from the current to the dictionary.
                if len(row_list) != 0:

                    # From the current row, retrieve the data
                    # from the column that contains the key.
                    key = row_list[key_column_index]

                    # Store the data from the current
                    # row into the dictionary.
                    dictionary[key] = row_list
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {filename} doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")

    except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {filename}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()