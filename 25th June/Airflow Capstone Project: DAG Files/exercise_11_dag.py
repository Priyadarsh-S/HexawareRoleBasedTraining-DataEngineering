from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 1, 1),
}

def create_temperature_file():
    os.makedirs('/tmp', exist_ok=True)
    content = """Monday, 34
Tuesday, 36
Wednesday, 31
Thursday, 38
Friday, 35
Saturday, 33
Sunday, 32"""
    with open('/tmp/temperature.txt', 'w') as f:
        f.write(content.strip())

def find_highest_temperature():
    temps = []
    with open('/tmp/temperature.txt', 'r') as f:
        for line in f:
            if line.strip():
                day, temp = line.split(',')
                temps.append(int(temp.strip()))
    return {"highest": max(temps), "average": sum(temps) / len(temps)}

def generate_weather_report(**kwargs):
    ti = kwargs['ti']
    metrics = ti.xcom_pull(task_ids='find_highest_temperature')
    with open('/tmp/weather_report.txt', 'w') as f:
        f.write(f"Highest Temperature = {metrics['highest']}\n")
        f.write(f"Average Temperature = {metrics['average']:.2f}\n")

with DAG(
        dag_id='exercise_11_temperature_analysis',
        default_args=default_args,
        schedule=None,
        catchup=False
) as dag:
    task1 = PythonOperator(task_id='create_temperature_file', python_callable=create_temperature_file)
    task2 = PythonOperator(task_id='find_highest_temperature', python_callable=find_highest_temperature)
    task3 = PythonOperator(task_id='generate_weather_report', python_callable=generate_weather_report)

    task1 >> task2 >> task3