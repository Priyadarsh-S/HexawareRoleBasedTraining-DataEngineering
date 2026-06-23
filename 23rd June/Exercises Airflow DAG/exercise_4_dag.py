from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def create_inventory():
    content = "Rice, 50\nOil, 7\nSoap, 35\nSugar, 10\nTea, 5\n"
    with open('/tmp/inventory.txt', 'w') as f:
        f.write(content)

def find_low_stock():
    low_stock_items = []
    with open('/tmp/inventory.txt', 'r') as f:
        for line in f:
            if line.strip():
                item, qty = line.split(',')
                if int(qty.strip()) < 15:
                    low_stock_items.append(item.strip())
    return low_stock_items

def generate_alert(ti):
    low_stock_items = ti.xcom_pull(task_ids='find_low_stock')
    with open('/tmp/alerts.txt', 'w') as f:
        for item in low_stock_items:
            f.write(f"{item}\n")

with DAG(
    dag_id='exercise_4_stock_alert',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='create_inventory',
        python_callable=create_inventory
    )
    task2 = PythonOperator(
        task_id='find_low_stock',
        python_callable=find_low_stock
    )
    task3 = PythonOperator(
        task_id='generate_alert',
        python_callable=generate_alert
    )

    task1 >> task2 >> task3