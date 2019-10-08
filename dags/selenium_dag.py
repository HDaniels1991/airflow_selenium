import json
from airflow.models import DAG
from airflow.operators.selenium_plugin import SeleniumOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import Variable
from selenium_scripts.wake_up_to_money import download_podcast
from datetime import datetime, timedelta

date = '{{ ds_nodash }}'
local_downloads = '{}/downloads'.format(cwd)

default_args = {
    'owner': 'harry_daniels',
    'wait_for_downstream': True,
    'start_date': datetime(2019, 10, 8),
    'end_date': datetime(2019, 10, 20),
    'retries': 3,
    'retries_delay': timedelta(minutes=5)
    }

dag = DAG('selenium_example_dag',
          schedule_interval='@daily',
          default_args=default_args)

start = DummyOperator(
    task_id='start',
    dag=dag)

get_podcast = SeleniumOperator(
    script=download_podcast,
    script_args=['https://www.bbc.co.uk/programmes/b0070lr5/episodes/downloads',
                 local_downloads,
                 date],
    task_id='get_podcast',
    dag=dag
)

end = DummyOperator(
    task_id='end',
    dag=dag)

start >> get_podcast
get_podcast >> end
