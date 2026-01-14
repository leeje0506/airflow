import pendulum
# Airflow 3.0 부터 아래 경로로 import 합니다.
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, Variable

# Airflow 2.10.5 이하 버전에서 실습시 아래 경로에서 import 하세요.
#from airflow import DAG
#from airflow.models import Variable
#from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_with_variable",
    schedule="10 9 * * *",
    start_date=pendulum.datetime(2023, 4, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:

    # variable 라이브러리 사용
    var_value = Variable.get("sample_key")
    bash_var_1 = BashOperator(
        task_id="bash_var_1",
        bash_command=f"echo variable:{var_value}"
    )

    # 권고:스케줄러 과부하를 줄이기 위해 진자 템플릿을 이용하여 오퍼레이터 내부에서 가져오는 방식
    bash_var_2 = BashOperator(
        task_id="bash_var_2",
        bash_command="echo variable:{{var.value.sample_key}}"
    )