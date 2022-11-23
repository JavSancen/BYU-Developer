with open("/home/francisco/Downloads/hr_system.txt") as hr_system:
    for line in hr_system:
        line = line.strip()

        parts = line.split(" ")

        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])

        salary1 = salary/24

        if job_title == "Engineer":
            salary1 += 1000

        #print(f"Name: {name}, Title: {job_title}")
        #print()
        print(f"{name} (ID: {id_number}), {job_title} - ${salary1:.2f}")