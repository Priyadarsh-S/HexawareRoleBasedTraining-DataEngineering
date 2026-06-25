from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 1, 1),
}

def create_transactions():
    os.makedirs('/tmp', exist_ok=True)
    content = """Deposit, 10000
Withdraw, 2500
Deposit, 4000
Withdraw, 1500
Deposit, 2000"""
    with open('/tmp/transactions.txt', 'w') as f:
        f.write(content.strip())

def calculate_balance():
    total_deposit = 0
    total_withdrawal = 0
    with open('/tmp/transactions.txt', 'r') as f:
        for line in f:
            if line.strip():
                action, amount = line.split(',')
                action = action.strip()
                amount = int(amount.strip())
                if action == "Deposit":
                    total_deposit += amount
                elif action == "Withdraw":
                    total_withdrawal += amount
    return {"deposit": total_deposit, "withdrawal": total_withdrawal, "balance": total_deposit - total_withdrawal}

def generate_account_report(**kwargs):
    ti = kwargs['ti']
    metrics = ti.xcom_pull(task_ids='calculate_balance')
    with open('/tmp/account_report.txt', 'w') as f:
        f.write(f"Total Deposit = {metrics['deposit']}\n")
        f.write(f"Total Withdrawal = {metrics['withdrawal']}\n")
        f.write(f"Final Balance = {metrics['balance']}\n")

with DAG(
        dag_id='exercise_12_bank_transactions',
        default_args=default_args,
        schedule=None,
        catchup=False
) as dag:
    task1 = PythonOperator(task_id='create_transactions', python_callable=create_transactions)
    task2 = PythonOperator(task_id='calculate_balance', python_callable=calculate_balance)
    task3 = PythonOperator(task_id='generate_account_report', python_callable=generate_account_report)

    task1 >> task2 >> task3