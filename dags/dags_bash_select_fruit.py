from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_select_fruit", # airflow에 뜨는 이름, 이거랑 파일이름 맞추기 권장
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"), # UTC는 글로벌, Asia/seoul
    catchup=False, # True : 현재 일자랑 start_date 사이의 모든 날짜를 실행해버림
) as dag:
    
    t1_orange = BashOperator(
        task_id = "ti_orange"
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE"
    )

    t2_avocado = BashOperator(
        task_id = "t2_avocado"
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO"
    )
    
    t1_orange >> t2_avocado

