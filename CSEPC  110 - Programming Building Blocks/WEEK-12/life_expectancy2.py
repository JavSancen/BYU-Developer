largest_age = -1
largest_year = 0

print("which year in database would you like to learn about?")
users_year = int(input("(for example, 1956, 2010, 1999... : ")
)

with open("/home/francisco/Downloads/life-expectancy.csv") as life_file:
    for lines in life_file:

        clean_lines = lines.strip()
        parts = clean_lines.split(",")

        country = parts[0]
        year = int(parts[1])
        age = float(parts[3])

        if year == users_year:

            if age > largest_age:

                largest_age = age
                largest_country = country

print(f"The country with the most life expectancy is: {country} whit {largest_year}")
print(f"It has {largest_age} life expectancy years.")
