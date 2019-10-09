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
    while True:
        time_0 = time.time()
        files = os.listdir(download_dir)
        if files:
            file = files[0]
            print(file)
            if date in file:
                print('file successfully downloaded to {}'.format(
                      os.path.join(download_dir, file)))
                break
            else:
                print('file not found.')
                print('sleeping for 5 and searching again.')
                time.sleep(5)
        elif time.time() - time_0 > 60:
            print('download timed out.')
            break

        
