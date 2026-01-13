from airflow.sdk import DAG, task
import pendulum

with DAG(
    dag_id="dags_python_text_decorator", # airflow에 뜨는 이름, 이거랑 파일이름 맞추기 권장
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2025, 12, 31, tz="Asia/Seoul"), # UTC는 글로벌, Asia/Seoul
    catchup=False, # True : 현재 일자랑 start_date 사이의 모든 날짜를 실행해버림
) as dag:
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)

    python_task_1 = print("task_decorator 실행")