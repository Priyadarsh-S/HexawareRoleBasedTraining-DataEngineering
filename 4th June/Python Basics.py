# PYTHON BASICS
print("Hello World!")

customer_name = "Rahul Sharma"
age = 28
salary = 75000.50
is_active = True

print(customer_name)
print(age)
print(salary)
print(is_active)

print(type(customer_name))
print(type(age))
print(type(salary))
print(type(is_active))

# IF ELSE
salary= 35000
if salary > 50000:
    print("High Income")
else:
    print("Normal Income")

# IF ELSE With Multiple Conditions
salary = 75000
experience = 5
if salary > 50000 and experience >= 3:
    print("Eligible")
else:
    print("Not Eligible")

# IF ELIF ELSE
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# Logical Operators
experience = 5
salary = 80000
if experience >= 3 and salary >= 50000:
    print("Eligible")
else:
    print("Not Eligible")

experience = 1
salary = 80000
if experience >= 3 and salary >= 50000:
    print("Eligible")
else:
    print("Not Eligible")

is_blocked = False
if not is_blocked:
    print("Login Allowed")

# LOOPS
for i in range(1, 6):
    print(i)

count = 1
while count <= 5:
    print(count)
    count += 1
