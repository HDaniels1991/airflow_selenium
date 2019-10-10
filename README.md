
# Selenium on Airflow

This repo demonstrates how to use the Selenium web driver, to automate a daily task on the web, in a Dockerized airflow environment. The environment used for this project was Ubuntu 18.04 on AWS EC2.

## Setting up the Airflow environment

Set up an environment and ensure that ports 22 and 8080 are open. 

ssh into the environment:

Clone the repo:
```
git clone https://github.com/HDaniels1991/airflow_selenium.git
```

Run the setup script, this will install docker engine and compose:
```
bash setup.sh
```

Create the required Docker network to enable the containers to communicate.
```
docker network create container_bridge
```

Create the named volume used to persist downloaded files.
```
docker volume create downloads
```

Extend the Selenium image to grant the Selenium user write permissions on the folder used for downloads.
```
docker build -t docker_selenium -f Dockerfile-selenium .
```

Extend the Airflow image to grant the container access to the host docker socket, install the requirements and create the downloads folder. The {AIRFLOW_USER_HOME} directory is also added to th python path to enable custom python modules.
```
docker build -t docker_airflow -f Dockerfile-airflow .
```

Run the docker compose:
```
docker-compose up
```

The Airflow webserver will be available at the following location:
* {Public DNS}:8080

## The Selenium Plugin

The Selenium Airflow plugin works by setting up a remote Selenium server on the host using Docker, connecting to the web-driver (standalone-chrome) and sending commands using the Python API. 

1. Create docker container.
2. Connect and configure driver.
3. Execute Python code.
4. Check Execution.
5. Remove container.

## Example Dag: Using Selenium to download a podcast each weekday and upload it to S3.

### Objective:

The Dag is designed to download a daily podcast from the BBC called wake up to money and upload it to S3.  

## Author:

Harry Daniels
