import bs4
import os
import time


def download_podcast(driver, url, download_dir, date):
    driver.get(url)
    soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
    ul = soup.find('ul', {'class': 'list-unstyled'})
    lq_li = ul.find_all('li')[1]
    download_link = lq_li.find('a')['href']
    download_link = 'http:' + download_link
    driver.get(download_link)
    # check for downloads
    file = 'WakeUpToMoney-{}.mp3'.format(date)
    downloaded_file = os.path.join(download_dir, file)
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

        
