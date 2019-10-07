
# Selenium on Airflow

This repo demonstrates how to use the Selenium web driver, to automate a daily task on the web, in a Dockerized airflow environment. The environment used for this project was Ubuntu 18.04 on AWS EC2.

## Setting up the Airflow environment

Set up an environment and ensure that ports 22 and 8080 are open. 

Clone the repo:
* git clone https://github.com/HDaniels1991/airflow_selenium.git

Run the setup script, this will install docker engine:
* bash setup.sh

Create the required Docker network and pull the selenium image.
* docker network create container_bridge
* docker pull selenium/standalone-chrome

Create the Docker image:
* docker build . -it docker_airflow

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

# WIP: Facebook blocks logins via Selenium. Searching for a new use case.

## Example: Scraping Tour De France GPX files from Strava

**Disclaimer** It explicitly states in the Strava terms and conditions that you cannot distribute or disclose any part of the Strava services using automated "scraping" and using an automated system, including "robots" to access the services in a manner that sends more request messages to Strava than humanily possible is prohibitted. The use case here is to provide a reproducable example task for the Selenium plugin.

### Objective:

For a 'hypothetical' visualisation project, I wanted to download from Strava, the GPX routes for each stage of the 2019 Tour de France, each day. The routes become publically available after the Pro riders upload their ride and can be downloaded from the UI.  

1. You will need a Strava login.
2. Login via Facebook.
3. Find a pro-rider.
4. Download the race for a specific execution date.

## Author:

Harry Daniels
