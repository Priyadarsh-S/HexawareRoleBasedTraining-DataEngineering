from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 1, 1),
}


def create_employee_file():
    os.makedirs('/tmp', exist_ok=True)
    content = """Rahul, 28
Priya, 31
Amit, 42
Sneha, 26
Kiran, 38"""
    with open('/tmp/employees.txt', 'w') as f:
        f.write(content.strip())


def calculate_average_age():
    ages = {}
    with open('/tmp/employees.txt', 'r') as f:
        for line in f:
            if line.strip():
                name, age = line.split(',')
                ages[name.strip()] = int(age.strip())

    youngest = min(ages, key=ages.get)
    oldest = max(ages, key=ages.get)
    avg_age = sum(ages.values()) / len(ages)

    return {"youngest": youngest, "oldest": oldest, "avg_age": avg_age}


def generate_age_report(**kwargs):
    ti = kwargs['ti']
    metrics = ti.xcom_pull(task_ids='calculate_average_age')
    with open('/tmp/age_report.txt', 'w') as f:
        f.write(f"Youngest Employee = {metrics['youngest']}\n")
        f.write(f"Oldest Employee = {metrics['oldest']}\n")
        f.write(f"Average Age = {metrics['avg_age']:.1f}\n")


with DAG(
        dag_id='exercise_13_employee_age',
        default_args=default_args,
        schedule=None,
        catchup=False
) as dag:
    task1 = PythonOperator(task_id='create_employee_file', python_callable=create_employee_file)
    task2 = PythonOperator(task_id='calculate_average_age', python_callable=calculate_average_age)
    task3 = PythonOperator(task_id='generate_age_report', python_callable=generate_age_report)

    task1 >> task2 >> task3