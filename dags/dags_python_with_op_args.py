from airflow.sdk import DAG, task
import pendulum

from airflow.operators.python import PythonOperator
from common.common_func import regist

with DAG(
    dag_id="dags_python_with_op_args", # airflow에 뜨는 이름, 이거랑 파일이름 맞추기 권장
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 12, 31, tz="Asia/Seoul"), # UTC는 글로벌, Asia/Seoul
    catchup=False, # True : 현재 일자랑 start_date 사이의 모든 날짜를 실행해버림
) as dag:

    regist_t1 = PythonOperator(
        task_id = 'regist_t1',
        python_callable = regist,
        op_args = ['aaa', 'man', 'kr', 'seoul']
    )

    regist_t1

    # @task(task_id="regist_t1")
    # def run(*op_args):
    #     regist(*op_args)
    #
    # regist_t1 = run(['aaa', 'man', 'kr', 'seoul'])
