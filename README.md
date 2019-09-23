
# Selenium on Airflow

This repo demonstrates how to use the Selenium web driver, to automate a daily task on the web, in a Dockerized airflow environment. 

## Setting up the Airflow environment

1. Spin up EC2:
	Distro: Ubuntu.
	Security Settings: Which ports.
2. Install Docker engine.
	Install git
	Install pip
3. Change Docker permissions?
3. Git pull.
4. Build dockerfile.
	Grant permissions, this extends puckel/docker-airflow image and grants the airflow user to the docker sock.
5. Run docker-compose.

## The Selenium Plugin

The Selenium Airflow plugin works by setting up a remote Selenium server on the host using Docker, connecting to the web-driver (standalone-chrome) and sending commands using the Python API. 

1. Create docker container.
2. Connect and configure driver.
3. Execute Python code.
4. Check Execution.
5. Remove container.

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
