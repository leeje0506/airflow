from __future__ import annotations

import datetime

import pendulum
import random

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from tornado.process import task_id

# dag에 대한 정의 (모든 dag에 다 필요)
with DAG(
    dag_id="dags_python_operator", # airflow에 뜨는 이름, 이거랑 파일이름 맞추기 권장
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 12, 31, tz="Asia/Seoul"), # UTC는 글로벌, Asia/Seoul
    catchup=False, # True : 현재 일자랑 start_date 사이의 모든 날짜를 실행해버림
) as dag:
    def select_fruit():
        fruit = ["BANANA", "ORANGE", "AVOCADO"]
        rand_int = random.randint(0,2)
        print(fruit[rand_int])

    py_t1 = PythonOperator(
        task_id = 'py_t1',
        python_callable=select_fruit
    )

    py_t1