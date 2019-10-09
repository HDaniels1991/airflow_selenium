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
    print('Testing for file')
    time0 = time.time()
    while True:
        files = os.listdir(download_dir)
        if files:
            file = files[0]
            if date in file:
                print('File downloading to {}'.format(
                    os.path.join(download_dir, file)
                ))
                time.sleep(30)
                break
            else:
                print('file not found, sleeping for 5 seconds')
                time.sleep(5)
        elif time.time() - time0 > 60:
            print('download timed out.')
            break
