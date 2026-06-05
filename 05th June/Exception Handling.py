# Exception Handling
try:
    a = 10
    b = 0
    result = a/b
    print(result)
except:
    print("Error Occurred")
print("Program Completed")

# Specific Exception
try:
    a =10
    b = 0
    result = a/b
except ZeroDivisionError:
    print("Cannot divide by zero")

# Another example
try:
    age = int(input("Enter Age: "))
    print(age)
except ValueError:
    print("Please enter numeric value")

# Multiple Exception
try:
    age = int(input("Enter Age: "))
    print(100 / age)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Age cannot be zero")

# Exception Object
try:
    num = int("abc")
except Exception as e:
    print(e)

# Else Block
try:
    num = 10
    print(num)
except:
    print("Error")
else:
    print("Success") # This block executes when there is no exception occurred

# Finally block
try:
    print(10 / 0)
except:
    print("Error")
finally:
    print("Connection Closed")

# Raise Error
salary = -1000
if salary < 0:
    raise ValueError("Salary cannot be negative")
