from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator", # airflow에 뜨는 이름, 이거랑 파일이름 맞추기 권장
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"), # UTC는 글로벌, Asia/seoul
    catchup=False, # True : 현재 일자랑 start_date 사이의 모든 날짜를 실행해버림
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"], # 옵션
    params={"example_key": "example_value"},
) as dag:
    
    t1 = EmptyOperator(
        task_id = "t1"
    )

    t2 = EmptyOperator(
        task_id = "t2"
    )

    t3 = EmptyOperator(
        task_id = "t3"
    )

    t4 = EmptyOperator(
        task_id = "t4"
    )

    t5 = EmptyOperator(
        task_id = "t5"
    )

    t6 = EmptyOperator(
        task_id = "t6"
    )

    t7 = EmptyOperator(
        task_id = "t7"
    )

    t8 = EmptyOperator(
        task_id = "t8"
    )

    t1 >> [t2,t3] >> t4
    t4 >> t5 
    [t4, t7] >> t6 >> t8