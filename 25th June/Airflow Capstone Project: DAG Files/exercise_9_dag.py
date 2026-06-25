from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 1, 1),
}

def create_result_file():
    os.makedirs('/tmp', exist_ok=True)
    content = """Rahul, Pass
Priya, Fail
Amit, Pass
Sneha, Pass
Kiran, Fail
Megha, Pass"""
    with open('/tmp/results.txt', 'w') as f:
        f.write(content.strip())

def count_pass_fail():
    results = {"Total Pass": 0, "Total Fail": 0}
    with open('/tmp/results.txt', 'r') as f:
        for line in f:
            if line.strip():
                name, status = line.split(',')
                status = status.strip()
                if status == "Pass":
                    results["Total Pass"] += 1
                elif status == "Fail":
                    results["Total Fail"] += 1
    return results

def generate_result_summary(**kwargs):
    ti = kwargs['ti']
    results = ti.xcom_pull(task_ids='count_pass_fail')
    with open('/tmp/result_summary.txt', 'w') as f:
        f.write(f"Total Pass = {results['Total Pass']}\n")
        f.write(f"Total Fail = {results['Total Fail']}\n")

with DAG(
        dag_id='exercise_9_exam_result',
        default_args=default_args,
        schedule=None,
        catchup=False
) as dag:
    task1 = PythonOperator(task_id='create_result_file', python_callable=create_result_file)
    task2 = PythonOperator(task_id='count_pass_fail', python_callable=count_pass_fail)
    task3 = PythonOperator(task_id='generate_result_summary', python_callable=generate_result_summary)

    task1 >> task2 >> task3