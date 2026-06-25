from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 1, 1),
}

def create_bill_file():
    os.makedirs('/tmp', exist_ok=True)
    content = """Rahul, 210
Priya, 180
Amit, 300
Sneha, 150
Kiran, 260"""
    with open('/tmp/electricity.txt', 'w') as f:
        f.write(content.strip())

def calculate_total_units():
    counts = 0
    total_units = 0
    with open('/tmp/electricity.txt', 'r') as f:
        for line in f:
            if line.strip():
                name, units = line.split(',')
                total_units += int(units.strip())
                counts += 1
    avg_units = total_units / counts if counts > 0 else 0
    return {"customers": counts, "total_units": total_units, "average_units": avg_units}

def generate_bill_summary(**kwargs):
    ti = kwargs['ti']
    metrics = ti.xcom_pull(task_ids='calculate_total_units')
    with open('/tmp/bill_summary.txt', 'w') as f:
        f.write(f"Customers = {metrics['customers']}\n")
        f.write(f"Total Units = {metrics['total_units']}\n")
        f.write(f"Average Units = {int(metrics['average_units'])}\n")

with DAG(
        dag_id='exercise_8_electricity_bill',
        default_args=default_args,
        schedule=None,
        catchup=False
) as dag:
    task1 = PythonOperator(task_id='create_bill_file', python_callable=create_bill_file)
    task2 = PythonOperator(task_id='calculate_total_units', python_callable=calculate_total_units)
    task3 = PythonOperator(task_id='generate_bill_summary', python_callable=generate_bill_summary)

    task1 >> task2 >> task3