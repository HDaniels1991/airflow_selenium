import os
import time
from datetime import datetime
import bs4


class Strava:
    '''
    The strava class provides a series of methods for interacting with Strava
    using the Selenium web driver.
    '''
    def __init__(self, driver, email, password):
        self.base_url = 'https://www.strava.com'
        self.driver = driver
        self.email = email
        self.password = password

    def login(self):
        '''
        Logs into Strava via Facebook
        '''
        #open strava
        url = os.path.join(self.base_url, 'login')
        self.driver.get(url)
        #login via Facebook
        self.driver.find_element_by_class_name('fb-button').click()
        self.driver.find_element_by_id('email').send_keys(self.email)
        self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_id('loginbutton').click()
        if 'dashboard' in self.driver.current_url:
            print('Successfully logged in to strava')
    
    @staticmethod
    def get_date(x):
        '''
        Returns formatted date string from html element with datetime attribute 
        '''
        date = x.find('time')['datetime']
        return str(datetime.strptime(date, '%Y-%m-%d %H:%M:%S %Z').date())
    
    def get_activity_feed(self, url):
        '''
        Returns the raw html list of activities from a Strava url
        '''
        self.driver.get(url)
        soup = bs4.BeautifulSoup(self.driver.page_source, 'lxml')
        feed = soup.findAll('div',{'class':'feed-entry'})
        if feed:
            return feed
        else:
            print('Feed not found')
        
    def get_activity(self, race_date, feed):
        '''
        Returns the strava activity link for a specific date from race feed.
        '''
        activity_index = [self.get_date(x) for x in feed].index(race_date)
        race_summary = feed[activity_index]
        activity = race_summary.find('strong').find('a')['href']
        activity_link = self.base_url + activity
        return activity_link
       
    def get_gpx(self, activity_link, download_dir):
        '''
        Downloads the activity GPX file from the Strava.
        '''
        self.driver.get(activity_link)
        self.driver.find_element_by_id('gpx-download').click()
        # Test for download.
        soup = bs4.BeautifulSoup(self.driver.page_source, 'lxml')
        downloaded_file = soup.find('h1').text.replace(' ','_') + '.gpx'
        downloaded_file = os.path.join(download_dir, downloaded_file)
        while True:
            time_0 = time.time()
            if os.path.isfile(downloaded_file):
                print('file successfully downloded to {}'.format(downloaded_file))
                break
            elif time.time() - time_0 > 60:
                print('download timed out.')
                break
            else:
                print('file not found. {} does not exist.'.format(downloaded_file))
                print('sleeping for 5 and searching again.')
                time.sleep(5)

                
def race_gpx(driver, email, password, url, date, download_folder):
    '''
    This function downloads the activity GPX file for a specific
    date from a strava athletes activity feed.
    '''
    strava = Strava(driver, email, password)
    strava.login()
    feed = strava.get_activity_feed(url)
    
    # Sometimes the page doesn't render correctly the first time,
    # The code below polls for the correct load.
    
    time0 = time.time()
    while True:
            if [x for x in [strava.get_date(x) for x in feed] if '2019-07' in x]:
                break
            elif time.time() - time0 > 60:
                print('Query timed-out')
                break
            else:
                print('Site not rendered correctly, trying again in 5 seconds')
                time.sleep(5)
                feed = strava.get_activity_feed(url)
    
    # Get activity
    activity_link = strava.get_activity(date, feed)

    # Get GPX
    strava.get_gpx(activity_link, download_folder)
                