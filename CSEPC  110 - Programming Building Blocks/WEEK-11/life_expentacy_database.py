import csv
import math
with open('/home/francisco/Downloads/life-expectancy.csv') as csvFile:

    csv_reader = csv.reader(csvFile, delimiter=",")
    line_count = 0

    id_max = 0
    id_min = 0
# this operators allows me to make easier the count for min and max
    value_max = -math.inf
    value_min = +math.inf

    for row in csv_reader:
        # this was the iterable for all the lines in alfabetic order
        #print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]}')
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f"Our year is {row[2]} and our value is {row[3]}")
            line_count += 1
            if float(row[3]) > value_max:
                id_max, value_max = row[2], float(row[3])
            elif float(row[3]) < value_min:
                id_min, value_min = row[2], float(row[3])

#This process the number of lines in the dataset and make a travel over each year value 
print(f"Processed lines: {line_count}")
#Then I print the max and min value
print(f"Max year {id_max} and max life expectancy age: {value_max}")
print(f"Max year {id_min} and min life expectancy age: {value_min}")

#NOTE: I used the row method because when I tried to print naming the parts as variables 
#the code doesnt work
