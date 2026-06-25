from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 1, 1),
}

def create_department_file():
    os.makedirs('/tmp', exist_ok=True)
    content = """IT, 45000
HR, 35000
Finance, 50000
IT, 55000
Finance, 40000
HR, 30000"""
    with open('/tmp/departments.txt', 'w') as f:
        f.write(content.strip())

def calculate_department_salary():
    totals = {}
    with open('/tmp/departments.txt', 'r') as f:
        for line in f:
            if line.strip():
                dept, salary = line.split(',')
                dept = dept.strip()
                salary = int(salary.strip())
                totals[dept] = totals.get(dept, 0) + salary
    return totals

def generate_department_report(**kwargs):
    ti = kwargs['ti']
    totals = ti.xcom_pull(task_ids='calculate_department_salary')
    with open('/tmp/department_report.txt', 'w') as f:
        f.write(f"IT={totals.get('IT', 0)}\n")
        f.write(f"HR={totals.get('HR', 0)}\n")
        f.write(f"Finance={totals.get('Finance', 0)}\n")

with DAG(
        dag_id='exercise_7_department_salary',
        default_args=default_args,
        schedule=None,
        catchup=False
) as dag:
    task1 = PythonOperator(task_id='create_department_file', python_callable=create_department_file)
    task2 = PythonOperator(task_id='calculate_department_salary', python_callable=calculate_department_salary)
    task3 = PythonOperator(task_id='generate_department_report', python_callable=generate_department_report)

    task1 >> task2 >> task3