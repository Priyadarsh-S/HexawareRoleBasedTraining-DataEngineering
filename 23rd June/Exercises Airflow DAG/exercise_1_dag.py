from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def create_file():
    content = (
        "Welcome to Apache Airflow\n"
        "Learning DAGS\n"
        "Learning Task Dependencies\n"
    )
    with open('/tmp/message.txt', 'w') as f:
        f.write(content)

def read_file():
    with open('/tmp/message.txt', 'r') as f:
        print(f.read())

with DAG(
    dag_id='exercise_1_create_read_file',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='create_file',
        python_callable=create_file
    )

    task2 = PythonOperator(
        task_id='read_file',
        python_callable=read_file
    )

    task1 >> task2
