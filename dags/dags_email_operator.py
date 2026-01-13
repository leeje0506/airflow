from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator", # airflow에 뜨는 이름, 이거랑 파일이름 맞추기 권장
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2025, 12, 31, tz="Asia/Seoul"), # UTC는 글로벌, Asia/Seoul
    catchup=False, # True : 현재 일자랑 start_date 사이의 모든 날짜를 실행해버림
) as dag:
    send_email_task = EmailOperator(
        task_id= "send_email_task",
        conn_id="conn_smtp_gmail",
        to="ju3391@naver.com",
        subject="Airflow 성공메일",
        html_content="Airflow 작업이 완료되었습니다."
    )