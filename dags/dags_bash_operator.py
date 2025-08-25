"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

# dag에 대한 정의 (모든 dag에 다 필요)
with DAG(
    dag_id="dags_bash_operator", # airflow에 뜨는 이름, 이거랑 파일이름 맞추기 권장
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/seoul"), # UTC는 글로벌, Asia/seoul
    catchup=False, # True : 현재 일자랑 start_date 사이의 모든 날짜를 실행해버림
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"], # 옵션
    params={"example_key": "example_value"},
) as dag:
   
    bash_t1 = BashOperator(
        task_id="bash_t1", # 객체명과 task id도 동일할 것을 권장
        bash_command="echo who am i",
    )
    
    bash_t2 = BashOperator(
        task_id="bash_t2", # 객체명과 task id도 동일할 것을 권장
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2 

