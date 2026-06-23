from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def create_marks_file():
    content = "Math, 80\nScience, 75\nEnglish, 90\nPython, 95\n"
    with open('/tmp/marks.txt', 'w') as f:
        f.write(content)

def calculate_average():
    total_marks = 0
    count = 0
    with open('/tmp/marks.txt', 'r') as f:
        for line in f:
            if line.strip():
                subject, mark = line.split(',')
                total_marks += int(mark.strip())
                count += 1
    avg = total_marks / count
    print(f"Average = {avg}")
    return avg

def generate_result(ti):
    avg = ti.xcom_pull(task_ids='calculate_average')
    result = "PASS" if avg >= 40 else "FAIL"

    with open('/tmp/result.txt', 'w') as f:
        f.write(f"Average Marks = {int(avg)}\nResult = {result}\n")

with DAG(
        dag_id='exercise_3_marks_processing',
        start_date=datetime(2026, 1, 1),
        schedule=None,
        catchup=False,
) as dag:
    task1 = PythonOperator(
        task_id='create_marks_file',
        python_callable=create_marks_file
    )
    task2 = PythonOperator(
        task_id='calculate_average',
        python_callable=calculate_average
    )
    task3 = PythonOperator(
        task_id='generate_result',
        python_callable=generate_result
    )

    task1 >> task2 >> task3