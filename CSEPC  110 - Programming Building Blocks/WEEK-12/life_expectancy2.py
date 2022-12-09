import csv
#
#with open("/home/francisco/Downloads/life-expectancy.csv", "r") as life_file:
#    csv_reader = csv.reader(life_file, delimiter = ',')
#    next(csv_reader)
#
#    for lines in csv_reader:
#        print("which year in database would you like to learn about?")
#        users_year = int(input("(for example, 1956, 2010, 1999... : "))
#        #clean_lines = csv_reader
#        #parts = clean_lines
##
#        #country = parts[0]
#        #year = parts[1]
#        #age = parts[3]
#
#        #for line in users_year(year):
#        largest_age = -1
#        largest_year = 0
#        if users_year('r'[1]) == 'r'[1]:
#            if 'r'[3] > largest_age:
#                largest_age = 'r'[3]
#                largest_country = 'r'[0]
#print(f"The country with the most life expectancy is: {'r'[0]} whit {largest_year}")
#print(f"It has {largest_age} life expectancy years.")
#chosen_year = input("choice ayear: ")

max_age = -1
country_max = ""

with open("/home/francisco/Downloads/life-expectancy.csv", "r") as file:
    csvreader = csv.reader(file, delimiter=':')
    next(csvreader)
    for row in file:

        #country = row[]
        print(row)

        for i in row:
            parts = i.split(" ")
        #parts = line.split(":")
            country = parts[0].strip()
            age = float(parts[3]).strip()
            years = parts[2].strip()

            print(country)
#
        #if years.lower() == chosen_year.lower():
        #    print(f"Year: {years}, country: {country}, age: {age}")
#
        #    if age > max_age:
#
        #        max_age = age
        #        country_max = country

#print(f"The Country with Highest expectancy life is: {country_max} in {chosen_year} with a expectancy of {age}")