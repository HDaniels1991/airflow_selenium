import json
from airflow.models import DAG
from airflow.operators.selenium_plugin import SeleniumOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import Variable
from selenium_scripts.strava_commands import race_gpx
from datetime import datetime, timedelta

strava_vars = json.loads(Variable.get('strava_variables_config'))
date = '{{ ds }}'

default_args = {
    'owner': 'harry_daniels',
    'wait_for_downstream': True,
    'start_date': datetime(2019, 7, 7),
    'end_date': datetime(2019, 7, 29),
    'retries': 3,
    'retries_delay': timedelta(minutes=5)
    }

dag = DAG('selenium_example_dag',
          schedule_interval='@daily',
          default_args=default_args)

start = DummyOperator(
    task_id='start',
    dag=dag)

get_tdf_gpx = SeleniumOperator(
    script=race_gpx,
    script_args=[strava_vars['email'],
                 strava_vars['password'],
                 strava_vars['url'],
                 date, strava_vars['download_folder']],
    task_id='get_tdf_gpx',
    dag=dag
)

end = DummyOperator(
    task_id='end',
    dag=dag)

start >> get_tdf_gpx
get_tdf_gpx >> end
