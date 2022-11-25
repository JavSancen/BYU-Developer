with open("/home/francisco/Downloads/life-expectancy.csv") as data_system:
    for line in data_system:
        line = line.strip()

        parts = line.split(",")

        entities = parts[0]
        codes = parts[1]
        years = parts[2]
        life_expectancies = float(parts[3])

max_value = None
min_value = None

for num in parts[3]:
    if (max_value is None or num > max_value):
        max_value = num
    elif (min_value is None or num < min_value):
        min_value = num

print('Maximum value:', max_value)
print('Minimum value:', min_value)

#for i in range(len(line)):
#    if select_year in line:
#        select_year = (input("select a year: "))
#        index2 = line.index(select_year)
#    entity = entities[i]
#    code = codes[i]
#    year = years[i]
#    life_expectancy = life_expectancies[i]

#if life_expectancies > highest_life_e:
#    highest_entity = life_expectancy
#    highest_entity = entity

#print(f"Highest Life expectancy at {select_year} is in {highest_entity} with {highest_life_e} years")






