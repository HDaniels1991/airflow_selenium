
FROM puckel/docker-airflow:1.10.4

ADD requirements.txt /usr/local/airflow/requirements.txt

USER root
RUN groupadd --gid 999 docker \
   && usermod -aG docker airflow 
USER airflow
