import csv
import numpy as np
import pandas as pd
import os

# Part 1 – File Handling
cnt = 0
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    print(next(reader))
    for row in reader:
        print(row)
        cnt += 1
print("Total Orders:", cnt)

# Part 2 - Revenue Analysis
revenue = 0
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue += (int(row[5]) * int(row[6]))
    print("Total Revenue:", revenue)

highest_order_value = 0
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        order_value = int(row[5]) * int(row[6])
        if order_value > highest_order_value:
            highest_order_value = order_value
    print("Highest Order Value:", highest_order_value)

lowest_order_value = float('inf')
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        order_value = int(row[5]) * int(row[6])
        if order_value < lowest_order_value:
            lowest_order_value = order_value
    print("Lowest Order Value:", lowest_order_value)

total_order_value = 0
cnt = 0
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total_order_value += int(row[5]) * int(row[6])
        cnt += 1
    print("Average Order Value:", total_order_value / cnt)

# Part 3 – Customer Analysis
customers = set()
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        customers.add(row[1])
print("Unique Customers:\n", customers)
print("Total Unique Customers:", len(customers))

name = ""
highest_purchase_amount = 0
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        purchase_amount = int(row[5]) * int(row[6])
        if purchase_amount > highest_purchase_amount:
            highest_purchase_amount = purchase_amount
            name = row[1]
print("Customer with highest purchase amount is", name, "with", highest_purchase_amount)

# Part 4 – Product Analysis
product_count = {}
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        if product in product_count:
            product_count[product] += int(row[5])
        else:
            product_count[product] = int(row[5])
print("Orders by Product:\n", product_count)

product_revenue = {}
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        revenue = int(row[5]) * int(row[6])
        product_revenue[product] = product_revenue.get(product, 0) + revenue
print("Revenue by Product:\n", product_revenue)

product_count = {}
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        if product in product_count:
            product_count[product] += int(row[5])
        else:
            product_count[product] = int(row[5])
print("Most sold product: ", max(product_count, key=product_count.get), "| Quantity: ", max(product_count.values()))
print("Least sold product: ", min(product_count, key=product_count.get), "| Quantity: ", min(product_count.values()))

category_revenue = {}
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        category = row[4]
        revenue = int(row[5]) * int(row[6])
        category_revenue[category] = category_revenue.get(category, 0) + revenue
print("Revenue by Category:\n", category_revenue)

# Part 5 – City Analysis
city_count = {}
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        city = row[2]
        city_count[city] = city_count.get(city, 0) + 1
print("Orders by City:\n", city_count)

city_revenue = {}
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        city = row[2]
        revenue = int(row[5]) * int(row[6])
        city_revenue[city] = city_revenue.get(city, 0) + revenue
print("Revenue by City:\n", city_revenue)
print("Highest revenue generating city is", max(city_revenue, key=city_revenue.get), "with", max(city_revenue.values()))

# Part 6 – Lists, Sets and Dictionaries
product_name = []
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product_name.append(row[3])
product_name.sort()
print("Sorted Product Names:\n", product_name)

unique_cities = set()
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        unique_cities.add(row[2])
print("Unique Cities:\n", unique_cities)

city_revenue = {}
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        city = row[2]
        revenue = int(row[5]) * int(row[6])
        city_revenue[city] = city_revenue.get(city, 0) + revenue
print("Dictionary, city : revenue\n", city_revenue)

product_count = {}
with open ("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        if product in product_count:
            product_count[product] += int(row[5])
        else:
            product_count[product] = int(row[5])
print("Dictionary, product : quantity_sold\n", product_count)

# Part 7 – Functions
def calculate_total_revenue():
    total_revenue = 0
    with open('orders.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total_revenue += int(row[5]) * int(row[6])
    return total_revenue
print("Total Revenue:", calculate_total_revenue())

def find_top_product():
    products = {}
    with open('orders.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            product = row[3]
            quantity = int(row[5])
            products[product] = products.get(product, 0) + quantity
    return max(products, key=products.get)
print("Top Product:", find_top_product())

def find_top_city():
    city_revenue = {}
    with open('orders.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            city = row[2]
            revenue = int(row[5]) * int(row[6])
            city_revenue[city] = city_revenue.get(city, 0) + revenue
    return max(city_revenue, key=city_revenue.get)
print("Top City:", find_top_city())

def average_order_value():
    total_revenue = calculate_total_revenue()
    cnt = 0
    with open('orders.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cnt += 1
    return total_revenue / cnt
print("Average Revenue:", average_order_value())

# Part 8 – Exception Handling
try:
    with open('orders.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV File Not Found")

print("Quantity of Products:")
quantity = []
with open('orders.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            quantity.append(int(row[5]))
        except ValueError:
            print("Invalid Quantity:", row)
    print(quantity)

print("Price of Products:")
price = []
with open('orders.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            price.append(int(row[6]))
        except ValueError:
            print("Invalid Price:", row)
    print(price)

# Part 9 – NumPy
order_values = []
with open('orders.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue = int(row[6]) * int(row[5])
        order_values.append(revenue)
arr = np.array(order_values)
print("Total Revenue:", np.sum(arr))
print("Average Revenue:", np.mean(arr))
print("Maximum Revenue:", np.max(arr))
print("Minimum Revenue:", np.min(arr))
print("Standard Deviation:", np.std(arr))

# Part 10 – Pandas
df = pd.read_csv('orders.csv')
print(df)

df["Revenue"] = df["quantity"] * df["price"]
print(df)

highest_value_orders = df.sort_values(by="Revenue", ascending=False)
print(highest_value_orders.head())

city_revenue = df.groupby("city")["Revenue"].sum()
print("City and its Revenue:\n", city_revenue)

product_revenue = df.groupby("product")["Revenue"].sum()
print("Product and its Revenue:\n", product_revenue)

product_sales = df.groupby("product")["quantity"].sum()
print("Top selling Products:\n", product_sales.sort_values(ascending=False))

print("City-wise Orders:\n", df["city"].value_counts())

# Report Generation
# sales_summary_report.txt
def generate_summary_report():
    total_orders = len(df)
    total_revenue = df["Revenue"].sum()
    average_order_value = df["Revenue"].mean()
    highest_order_value = df["Revenue"].max()
    lowest_order_value = df["Revenue"].min()
    category_revenue = df.groupby("category")["Revenue"].sum()
    top_product = product_sales.idxmax()
    top_city = city_revenue.idxmax()
    with open("sales_summary_report.txt", "w") as file:
        file.write(f"Total Orders: {total_orders}\n")
        file.write(f"Total Revenue: {total_revenue}\n")
        file.write(f"Average Order Value: {average_order_value}\n")
        file.write(f"Highest Order Value: {highest_order_value}\n")
        file.write(f"Lowest Order Value: {lowest_order_value}\n\n")
        file.write(f"Revenue By City\n {str(city_revenue)}\n\n")
        file.write(f"Revenue By Category\n {str(category_revenue)}\n\n")
        file.write(f"Top Selling Product: {top_product}\n")
        file.write(f"Top Revenue Generating City: {top_city}")
generate_summary_report()
print("Report Generated Successfully.")

# Bonus Tasks
# high_value_orders.csv
high_value_orders = df[df["Revenue"] > 50000]
high_value_orders.to_csv("high_value_orders.csv", index=False)
print("high_value_orders.csv File Created.")

# electronics_orders.csv
electronics_orders = df[df["category"] == "Electronics"]
electronics_orders.to_csv("electronics_orders.csv", index=False)
print("electronics_orders.csv File Created.")

# Menu Driven Application
while True:
    print("\n--- MENU DRIVEN APPLICATION ---")
    print("1. View Orders\n2. Revenue Analysis\n3. Product Analysis\n4. City Analysis\n5. Export Reports\n6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print(df)
    elif choice == 2:
        total_revenue = df["Revenue"].sum()
        average_order_value = df["Revenue"].mean()
        print(f"Total Revenue: {total_revenue}")
        print(f"Average Revenue: {average_order_value}")
    elif choice == 3:
        print(product_sales)
    elif choice == 4:
        print(city_revenue)
    elif choice == 5:
        generate_summary_report()
        print("Report Exported.")
        print("Report saved at:")
        print(os.path.abspath("sales_summary_report.txt"))
    elif choice == 6:
        break
    else:
        print("Invalid Choice. Try Again")
