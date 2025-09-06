from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def print_hello():
    print("Hello World!")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 9, 6),
    "email": ["your-email@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "hello_world",
    default_args=default_args,
    description="A simple hello world DAG",
    schedule_interval=timedelta(days=1),
)

hello_task = PythonOperator(
    task_id="hello_task",
    python_callable=print_hello,
    dag=dag,
)
