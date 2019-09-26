
from airflow.hooks.base_hook import BaseHook
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import logging
import docker
import os
import time


class SeleniumHook(BaseHook):
    '''
    Creates a Selenium Docker container on the host and controls the
    browser by sending commands to the remote server.
    '''
    def __init__(self):
        print('initialised hook')
        pass

    def create_container(self):
        '''
        Creates the selenium docker container
        '''
        cwd = os.getcwd()
        self.local_downloads = os.path.join(cwd, 'downloads')
        self.sel_downloads = '/home/seluser/downloads'
        volumes = ['{}:{}'.format(self.local_downloads,
                                  self.sel_downloads),
                   '/dev/shm:/dev/shm']
        client = docker.from_env()
        container = client.containers.run('selenium/standalone-chrome',
                                          volumes=volumes,
                                          ports={'4444/tcp': 4444},  # local
                                          network='container_bridge',
                                          detach=True)
        self.container = container
        cli = docker.APIClient()
        self.container_ip = cli.inspect_container(
            container.id)['NetworkSettings']['IPAddress']

    def create_driver(self):
        '''
        creates and configure the remote Selenium webdriver.
        '''
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920x1080")
        chrome_driver = '{}:4444/wd/hub'.format(self.container_ip)
        chrome_driver = '{}:4444/wd/hub'.format('http://127.0.0.1')  # local
        # wait for remote, unless timeout.
        while True:
            try:
                driver = webdriver.Remote(
                    command_executor=chrome_driver,
                    desired_capabilities=DesiredCapabilities.CHROME,
                    options=options)
                print('remote ready')
                break
            except:
                print('remote not ready, sleeping for ten seconds.')
                time.sleep(10)
        # Enable downloads in headless chrome.
        driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow',
                             'downloadPath': self.sel_downloads}}
        driver.execute("send_command", params)
        self.driver = driver

    def run_script(self, script, args):
        '''
        This is a wrapper around python scripts which sends commands to
        the docker container. The script must use the variable driver.
        '''
        script(self.driver, *args)

    def remove_container(self):
        '''
        This removes the Selenium container.
        '''
        self.container.remove(force=True)
        print('Removed container: {}'.format(self.container.id))
