# LISTS
cities = ["Hyderabad", "Mumbai", "Delhi"]
print(cities[0])
print(cities[1])
print(cities[2])

# Negative Indexing
print(cities[-1])
print(cities[-2])

# Update an Element
cities[1] = "Bangalore"
print(cities[1])

# Append
cities.append("Chennai")
print(cities)

# Insert
cities.insert(1, "Pune")
print(cities)

# Multiple Values
cities.extend(["Cochin", "Pondicherry"])
print(cities)

# Membership Operator
print("Mumbai" in cities)
print("Pune" in cities)

print(cities.index("Delhi"))

# Sort
cities.sort()
print(cities)

# Remove
cities.remove("Pondicherry")
print(cities)

cities.pop()
print(cities) # Removes the last element
cities.pop(3) # Removes the element in the given index
print(cities)

del cities[0]
print(cities)

cities.clear()
print(cities)
print((len(cities)))

# TUPLES
cities = ("Hyderabad", "Mumbai", "Delhi", "Chennai", "Pune")
print(cities)
print((cities[0]))
print((cities[1]))
print((cities[-1]))
print((cities[-2]))
print(len(cities))
print(cities[1:4])
# cities[1] = "Bangalore" Can't update tuples, it'll result in error.

# Packing and Unpacking
employee = (101, "Rahul", 75000)
print(employee)
emp_id, emp_name, salary = employee
print(emp_id)
print(emp_name)
print(salary)

# Multiple Values
def get_employee():
    return 101, "Rahul", 75000
result = get_employee()
print(result)
# Each row is represented as a Tuple
record = (
    101,
    "Rahul",
    "Hyderabad",
    75000
)
print(record)

# SETS
cities = {"Hyderabad", "Mumbai", "Delhi"}
print(cities)
cities = {"Hyderabad", "Mumbai", "Delhi", "Mumbai"}
print(cities)

# Remove Duplicates from List
# cities = ["Hyderabad", "Mumbai", "Delhi", "Mumbai"]
# unique_cities = set(cities)
# print(unique_cities)

cities.add("Chennai")
print(cities)
cities.update(["Delhi", "Pune"])
print(cities)
cities.remove("Mumbai")
print(cities)
cities.discard("Pune") #No Error when data is not present in the set
print(cities)

set1 = {"Python", "SQL"}
set2 = {"MongoDB", "Python"}
result = set1.union(set2)
print(result)
result = set1.intersection(set2)
print(result)
result = set1.difference(set2)
print(result)
result = set2.difference(set1)
print(result)
result = set1.symmetric_difference(set2)
print(result)

# DICTIONARY
customer= {
    "customer_id": 101,
    "name": "Rahul",
    "city": "Hyderabad"
}
print(customer)
print(customer["name"])
print(customer["city"])
print(customer.get("name")) # safe
print(customer.get("salary"))

# Add New Key Value Pair
customer["salary"] = 75000
print(customer)
# Update
customer["name"] = "Rahul Sharma"
print(customer)

customer.pop("salary")
print(customer)
del customer["city"]
print(customer)