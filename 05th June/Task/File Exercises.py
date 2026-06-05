# Test doc Exercises (File Operations)
with open("employees.txt", "r") as file:
    print(file.read())

with open("employees.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("employees.txt", "r") as file:
    cnt = len(file.readlines())
    print("Total Employees =", cnt)

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        print(data[1])

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if data[4] == "Hyderabad":
            print(line.strip())

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if data[4] == "Bangalore":
            print(line.strip())

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if int(data[3]) > 80000:
            print(line.strip())

highest_salary = 0
with open("employees.txt", "r") as file:
    for line in file:
        salary = int(line.strip().split(",")[3])
        if salary > highest_salary:
            highest_salary = salary
    print("Highest Salary =", highest_salary)

lowest_salary = float('inf')
with open("employees.txt", "r") as file:
    for line in file:
        salary = int(line.strip().split(",")[3])
        if salary < lowest_salary:
            lowest_salary = salary
    print("Lowest Salary =", lowest_salary)

total_salary = 0
cnt = 0
with open("employees.txt", "r") as file:
    for line in file:
        salary = int(line.strip().split(",")[3])
        total_salary += salary
        cnt += 1
    print("Average Salary =", total_salary / cnt)

total_salary = 0
with open("employees.txt", "r") as file:
    for line in file:
        total_salary += int(line.strip().split(",")[3])
    print("Total Salary =", total_salary)

cnt = 0
with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if data[2] == "AI Engineering":
            cnt += 1
    print("Total Employees in AI Engineering =", cnt)

cnt = 0
with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if data[2] == "Data Engineering":
            cnt += 1
    print("Total Employees in Data Engineering =", cnt)

with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if data[2] == "AI Engineering":
            print(line.strip())

# high_salary_employees file
with open("employees.txt", "r") as file, open("high_salary_employees.txt", "w") as nfile:
    for line in file:
        salary = int(line.strip().split(",")[3])
        if salary > 80000:
            nfile.write(line)
    print("high_salary_employees file created")

# hyderabad_employees
with open("employees.txt", "r") as file, open("hyderabad_employees.txt", "w") as nfile:
    for line in file:
        data = line.strip().split(",")
        if data[4] == "Hyderabad":
            nfile.write(line)
    print("hyderabad_employees file created")

cities = set()
with open("employees.txt", "r") as file:
    for line in file:
        cities.add(line.strip().split(",")[4])
for city in cities:
    print(city)
print("Total cities =", len(cities))

departments = {}
with open("employees.txt", "r") as file:
    for line in file:
        dept = line.strip().split(",")[2]
        departments[dept] = departments.get(dept, 0) + 1
for dept, cnt in departments.items():
    print(dept, "=", cnt)

highest_salary = 0
name = ""
with open("employees.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        salary = int(data[3])
        if salary > highest_salary:
            highest_salary = salary
            name = data[1]
print(name)
print(highest_salary)

#employee_report file
cnt = 0
highest_salary =0
lowest_salary = float('inf')
total_salary = 0
with open("employees.txt", "r") as file:
    for line in file:
        salary = int(line.strip().split(",")[3])
        if salary < lowest_salary:
            lowest_salary = salary
        if salary > highest_salary:
            highest_salary = salary
        cnt += 1
        total_salary += salary
avg_salary = total_salary / cnt
with open("employee_report.txt", "w") as file:
    file.write(f"Total Employees: {cnt}\n")
    file.write(f"Highest Salary: {highest_salary}\n")
    file.write(f"Lowest Salary: {lowest_salary}\n")
    file.write(f"Average Salary: {avg_salary}\n")
    file.write(f"Total Salary: {total_salary}")
print("employee_report file created")
