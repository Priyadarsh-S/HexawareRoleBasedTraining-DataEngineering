from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import csv
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 1, 1),
}

def create_orders():
    os.makedirs('/tmp', exist_ok=True)
    content = """product, quantity, price
Laptop, 1,70000
Mouse, 4,500
Monitor, 2,12000
Keyboard, 3,1500"""
    with open('/tmp/orders.csv', 'w') as f:
        f.write(content.strip())

def calculate_order_value():
    total_revenue = 0
    highest_revenue = 0
    highest_product = ""

    with open('/tmp/orders.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            if row:
                product = row[0].strip()
                qty = int(row[1].strip())
                price = int(row[2].strip())
                revenue = qty * price
                total_revenue += revenue
                if revenue > highest_revenue:
                    highest_revenue = revenue
                    highest_product = product

    return {"total_revenue": total_revenue, "highest_selling_product": highest_product}

def generate_sales_report(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='calculate_order_value')
    with open('/tmp/sales_report.txt', 'w') as f:
        f.write(f"Total Revenue = {data['total_revenue']}\n")
        f.write(f"Highest Selling Product = {data['highest_selling_product']}\n")

with DAG(
        dag_id='exercise_10_online_orders',
        default_args=default_args,
        schedule=None,
        catchup=False
) as dag:
    task1 = PythonOperator(task_id='create_orders', python_callable=create_orders)
    task2 = PythonOperator(task_id='calculate_order_value', python_callable=calculate_order_value)
    task3 = PythonOperator(task_id='generate_sales_report', python_callable=generate_sales_report)

    task1 >> task2 >> task3