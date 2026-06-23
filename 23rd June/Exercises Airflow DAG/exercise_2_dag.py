from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def create_salary_file():
    content = "Rahul, 45000\nPriya, 52000\nAmit, 61000\nSneha, 48000\n"
    with open('/tmp/employees.txt', 'w') as f:
        f.write(content)

def calculate_total_salary():
    total = 0
    with open('/tmp/employees.txt', 'r') as f:
        for line in f:
            if line.strip():
                name, salary = line.split(',')
                total += int(salary.strip())
    print(f"Total Salary = {total}")
    return total

def generate_report(ti):
    total_salary = ti.xcom_pull(task_ids='calculate_total_salary')

    with open('/tmp/employees.txt', 'r') as f:
        employees = [line for line in f if line.strip()]

    report_content = (
        "Salary Report\n"
        f"Employees = {len(employees)}\n"
        f"Total Salary = {total_salary}\n"
    )
    with open('/tmp/report.txt', 'w') as f:
        f.write(report_content)

with DAG(
        dag_id='exercise_2_salary_report',
        start_date=datetime(2026, 1, 1),
        schedule=None,
        catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='create_salary_file',
        python_callable=create_salary_file
    )
    task2 = PythonOperator(
        task_id='calculate_total_salary',
        python_callable=calculate_total_salary
    )
    task3 = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report
    )

    task1 >> task2 >> task3