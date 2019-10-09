
# Selenium on Airflow

This repo demonstrates how to use the Selenium web driver, to automate a daily task on the web, in a Dockerized airflow environment. The environment used for this project was Ubuntu 18.04 on AWS EC2.

## Setting up the Airflow environment

Set up an environment and ensure that ports 22 and 8080 are open. 

Clone the repo:
* git clone https://github.com/HDaniels1991/airflow_selenium.git

Run the setup script, this will install docker engine:
* bash setup.sh

Create the required Docker network to enable the containers to communicate.
* docker network create container_bridge

Extend the Selenium image to grant the Selenium user write permissions on the container used for downloads. This will be used as a mounted volume later.
* docker build -t docker_selenium -f Dockerfile-selenium .

Create the Airflow docker image:
* docker build . -t docker_airflow

Run the docker compose:
* docker-compose -f docker-compose-CeleryExecutor.yml

The Airflow webserver will be available at the following location:
* {Public DNS}:8080

## The Selenium Plugin

The Selenium Airflow plugin works by setting up a remote Selenium server on the host using Docker, connecting to the web-driver (standalone-chrome) and sending commands using the Python API. 

1. Create docker container.
2. Connect and configure driver.
3. Execute Python code.
4. Check Execution.
5. Remove container.

## Example Dag: Using Selenium to download a podcast each weekday and email it to an end user.

### Objective:

The Dag is designed to download a daily podcast from the BBC called wake up to money and email it to the end user.  

A local example of the selenium script can be found in the selenium_on_docker.ipynb file.

## Author:

Harry Daniels
