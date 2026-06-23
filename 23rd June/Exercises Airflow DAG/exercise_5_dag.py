from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def create_attendance():
    content = "Rahul, Present\nPriya, Present\nAmit, Absent\nSneha, Present\nKiran, Absent\n"
    with open('/tmp/attendance.txt', 'w') as f:
        f.write(content)

def count_present():
    count = 0
    with open('/tmp/attendance.txt', 'r') as f:
        for line in f:
            if "Present" in line:
                count += 1
    return count

def count_absent():
    count = 0
    with open('/tmp/attendance.txt', 'r') as f:
        for line in f:
            if "Absent" in line:
                count += 1
    return count

def generate_summary(ti):
    present = ti.xcom_pull(task_ids='count_present')
    absent = ti.xcom_pull(task_ids='count_absent')
    total = present + absent

    summary = (
        f"Total Students = {total}\n"
        f"Present = {present}\n"
        f"Absent = {absent}\n"
    )
    with open('/tmp/attendance_report.txt', 'w') as f:
        f.write(summary)

with DAG(
        dag_id='exercise_5_attendance_report',
        start_date=datetime(2026, 1, 1),
        schedule=None,
        catchup=False,
) as dag:
    task1 = PythonOperator(
        task_id='create_attendance',
        python_callable=create_attendance
    )
    task2 = PythonOperator(
        task_id='count_present',
        python_callable=count_present
    )
    task3 = PythonOperator(
        task_id='count_absent',
        python_callable=count_absent
    )
    task4 = PythonOperator(
        task_id='generate_summary',
        python_callable=generate_summary
    )

    task1 >> [task2, task3] >> task4