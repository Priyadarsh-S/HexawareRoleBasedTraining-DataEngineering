# File Operations
file = open("employees.txt", "r")
data = file.read()
print(data)
file.close()

file = open("employees.txt", "r")
print(file.readline()) # To read single line

# To read multiple lines
lines = file.readlines()
print(lines)
file.close()

# Automatically close the file object
with open("employees.txt", "r") as file:
    data = file.read()
    print(data)

# Write and Append
with open("employees1.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n") # Even we execute again, it'll override the contents, doesn't repeat it

with open("employees1.txt", "a") as file:
    file.write("Amit\n")


# JSON File Handling
import json

employees = [
    {
        "employee_id": 101,
        "name": "Rahul Sharma",
        "department": "Data Engineering",
        "salary": 75000,
        "city": "Hyderabad"
    },
    {
        "employee_id": 102,
        "name": "Priya Reddy",
        "department": "AI Engineering",
        "salary": 85000,
        "city": "Bangalore"
    },
    {
        "employee_id": 103,
        "name": "Amit Kumar",
        "department": "Data Engineering",
        "salary": 65000,
        "city": "Mumbai"
    },
    {
        "employee_id": 104,
        "name": "Sneha Patel",
        "department": "Data Science",
        "salary": 95000,
        "city": "Chennai"
    },
    {
        "employee_id": 105,
        "name": "Farhan Ali",
        "department": "Cloud Engineering",
        "salary": 80000,
        "city": "Delhi"
    }
]

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
print("JSON file created successfully")

with open("employees.json", "r") as file:
    employees = json.load(file)
print(employees)

# Print All Employees
for employee in employees:
    print(employee)
for employee in employees:
    print(employee["name"]) # Print names of employees
print(len(employees)) # To find number of employees

# Highest Salary
highest_salary = 0
name = ""
for employee in employees:
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
        name = employee["name"]
print(f"Employee {name} is with highest salary: {highest_salary}")

# Average Salary
total_salary = 0
for employee in employees:
    total_salary += employee["salary"]
print("Average salary: ", total_salary/len(employees))

# Data Engineering Employees
for employee in employees:
    if employee["department"] == "Data Engineering":
        print(employee)

# Employees with more than 80000 salary
for employee in employees:
    if employee["salary"] > 80000:
        print(employee)

# Update Salary of an Employee
with open("employees.json", "r") as file:
    employees = json.load(file)
for employee in employees:
    if employee["employee_id"] == 101:
        employee["salary"] = 70000
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
print("Salary updated.")

# Add new employee
with open("employees.json", "r") as file:
    employees = json.load(file)
new_employee = {
    "employee_id": 106,
    "name": "Preeti Sharma",
    "department": "CSBS",
    "salary": 75000,
    "city": "Chennai"
}
employees.append(new_employee)
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
print("New employee added.")

# Delete employee
with open("employees.json", "r") as file:
    employees = json.load(file)
employees = [employee for employee in employees if employee["employee_id"] != 104]
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
print("Employee deleted.")


# CSV File Handling
import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# To ignore the header
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[1]) # Display Employee Names

# Count Employees
cnt = 0
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cnt += 1
print("Total Employees:", cnt)

# Highest Salary
highest_salary = 0
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if int(row[3]) > highest_salary:
            highest_salary = int(row[3])
    print("Highest Salary:", highest_salary)

# Lowest Salary
lowest_salary = float("inf")
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if int(row[3]) < lowest_salary:
            lowest_salary = int(row[3])
    print("Lowest Salary:", lowest_salary)

# Average Salary and Total Salary
total_salary = 0
cnt = 0
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total_salary += int(row[3])
        cnt += 1
    print("Average salary:", total_salary/cnt)
    print("Total Salary:", total_salary)

# Display Hyderabad employees
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[4] == "Hyderabad":
            print(row)

# Display AI Engineering employees
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[2] == "AI Engineering":
            print(row)

# Display employees earning above ₹80,000
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if int(row[3]) > 80000:
            print(row)
