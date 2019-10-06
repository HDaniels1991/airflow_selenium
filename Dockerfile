
FROM puckel/docker-airflow:1.10.4

ARG AIRFLOW_USER_HOME=/usr/local/airflow
ENV PYTHONPATH=$PYTHONPATH:${AIRFLOW_USER_HOME}

COPY requirements.txt /requirements.txt

USER root
RUN groupadd --gid 999 docker \
   && usermod -aG docker airflow 
USER airflow


