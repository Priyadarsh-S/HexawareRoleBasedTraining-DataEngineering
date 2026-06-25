from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 1, 1),
}

def create_enrollment_file():
    os.makedirs('/tmp', exist_ok=True)
    content = """Python, Rahul
Python, Priya
SQL, Amit
Python, Sneha
Power BI, Kiran
SQL, Megha
Power BI, Arjun"""
    with open('/tmp/enrollments.txt', 'w') as f:
        f.write(content.strip())

def count_students():
    counts = {}
    with open('/tmp/enrollments.txt', 'r') as f:
        for line in f:
            if line.strip():
                course, student = line.split(',')
                course = course.strip()
                counts[course] = counts.get(course, 0) + 1
    return counts

def generate_course_report(**kwargs):
    ti = kwargs['ti']
    counts = ti.xcom_pull(task_ids='count_students')
    with open('/tmp/course_report.txt', 'w') as f:
        f.write(f"Python = {counts.get('Python', 0)}\n")
        f.write(f"SQL = {counts.get('SQL', 0)}\n")
        f.write(f"Power BI = {counts.get('Power BI', 0)}\n")

with DAG(
        dag_id='exercise_14_course_enrollment',
        default_args=default_args,
        schedule=None,
        catchup=False
) as dag:
    task1 = PythonOperator(task_id='create_enrollment_file', python_callable=create_enrollment_file)
    task2 = PythonOperator(task_id='count_students', python_callable=count_students)
    task3 = PythonOperator(task_id='generate_course_report', python_callable=generate_course_report)

    task1 >> task2 >> task3