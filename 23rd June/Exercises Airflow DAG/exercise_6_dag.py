import csv
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def create_csv():
    content = (
        "product, quantity, price\n"
        "Laptop, 2, 70000\n"
        "Mouse, 5, 500\n"
        "Keyboard, 3, 1200\n"
    )
    with open('/tmp/sales.csv', 'w') as f:
        f.write(content)

def read_csv():
    rows = []
    with open('/tmp/sales.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            clean_row = {k.strip(): v.strip() for k, v in row.items()}
            rows.append(clean_row)
    return rows

def calculate_revenue(ti):
    rows = ti.xcom_pull(task_ids='read_csv')
    revenues = {}
    total_revenue = 0

    for row in rows:
        prod = row['product']
        qty = int(row['quantity'])
        price = int(row['price'])
        rev = qty * price
        revenues[prod] = rev
        total_revenue += rev

    return {"breakdown": revenues, "total": total_revenue}

def create_summary(ti):
    data = ti.xcom_pull(task_ids='calculate_revenue')
    breakdown = data['breakdown']
    total = data['total']

    with open('/tmp/sales_summary.txt', 'w') as f:
        for prod, rev in breakdown.items():
            f.write(f"{prod} = {rev}\n")
        f.write(f"Total Revenue = {total}\n")

with DAG(
        dag_id='exercise_6_csv_processing',
        start_date=datetime(2026, 1, 1),
        schedule=None,
        catchup=False,
) as dag:
    task1 = PythonOperator(task_id='create_csv', python_callable=create_csv)
    task2 = PythonOperator(task_id='read_csv', python_callable=read_csv)
    task3 = PythonOperator(task_id='calculate_revenue', python_callable=calculate_revenue)
    task4 = PythonOperator(task_id='create_summary', python_callable=create_summary)

    task1 >> task2 >> task3 >> task4