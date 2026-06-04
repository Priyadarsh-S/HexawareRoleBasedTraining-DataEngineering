# Dataset 1: Employee Salaries (List)
salaries = [45000, 55000, 65000, 75000, 85000]
print(salaries)
print(max(salaries))
print(min(salaries))
print("Average Salary: ", sum(salaries)/len(salaries))
salaries.extend([95000, 105000])
print(salaries)
salaries.remove(55000)
print(salaries)
salaries.sort()
print("Ascending Salaries: ", salaries)
salaries.sort(reverse=True)
print("Descending Salaries: ", salaries)
print("Second Highest Salary: ", salaries[1])
print("Salaries greater than 70,000: ")
for salary in salaries:
    if salary > 70000:
        print(salary)

# Dataset 2: Employee Record (Tuple)
employee = (
    101,
    "Rahul Sharma",
    "Data Engineering",
    75000
)
print(employee)
print("Employee Name: ", employee[1])
print("Employee Department", employee[2])
emp_id, emp_name, dept, salary = employee
print("Employee ID: ", emp_id)
print("Employee Name: ", emp_name)
print("Employee Department: ", dept)
print("Salary: ", salary)
print("Length: ", len(employee))
print("First Element: ", employee[0])
print("Last Element: ", employee[-1])

# Dataset 3: Batch Students (Set)
batch_a = {
    "Rahul",
    "Priya",
    "Amit",
    "Sneha",
    "Farhan"
}
batch_b = {
    "Priya",
    "Sneha",
    "Neha",
    "Arjun",
    "Farhan"
}
print(batch_a.intersection(batch_b))
print(batch_a.difference(batch_b))
print(batch_b.difference(batch_a))
print(batch_a.union(batch_b))
print(batch_a.symmetric_difference(batch_b))

# Dataset 4: Employee Dictionary
employee_info = {
    "employee_id": 101,
    "name": "Rahul Sharma",
    "department": "Data Engineering",
    "salary": 75000,
    "city": "Hyderabad"
}
print("Employee Name: ", employee_info["name"])
print("Department and City: ", employee_info["department"], employee_info["city"])
employee_info["experience"] = 5
print(employee_info)
employee_info["salary"] = 85000
print(employee_info)
employee_info.pop("city")
print(employee_info)
print("Keys: ", employee_info.keys())
print("Values: ", employee_info.values())
print("All key-value pairs: ", employee_info)

# Dataset 5: List of Dictionaries
employees = [
    {"id": 101, "name": "Rahul", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Priya", "department": "HR", "salary": 70000},
    {"id": 103, "name": "Amit", "department": "IT", "salary": 60000},
    {"id": 104, "name": "Sneha", "department": "Finance", "salary": 80000},
    { "id": 105, "name": "Farhan", "department": "IT", "salary": 90000}
]
print("Name of the employees: ")
for emp in employees:
    print(emp["name"])
for emp in employees:
    if emp["department"] == "IT":
        print(emp)
highest_salary = max(employees, key=lambda emp: emp["salary"])
print("Highest Salary: ", highest_salary)
lowest_salary = min(employees, key=lambda emp: emp["salary"])
print("Lowest Salary: ", lowest_salary)
avg_salary = sum(emp["salary"] for emp in employees) / len(employees)
print("Average salary: ", avg_salary)
total_salary = sum(emp["salary"] for emp in employees)
print("Total salary: ", total_salary)
for emp in employees:
    if emp["salary"] > 70000:
        print(emp)
cnt=0
for emp in employees:
    if emp["department"] == "IT":
        cnt+=1
print("Employee Count in IT Department: ", cnt)
sorted_employees = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
print("Employee names sorted by salary (desc): ")
for emp in sorted_employees:
    print(emp["name"])
print("Second highest salary: ", sorted_employees[1])
departments = {emp["department"] for emp in employees}
print(departments)