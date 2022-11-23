with open("/home/francisco/Downloads/life-expectancy.csv") as data_system:
    for line in data_system:
        line = line.strip()

        parts = line.split(",")

        entity = parts[0]
        code = parts[1]
        year = parts[2]
        life_expectancy = parts[3]
