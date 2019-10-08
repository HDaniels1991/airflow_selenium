import bs4

def download_podcast(driver, url, local_downloads):
    driver.get(url)
    soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
    ul = soup.find('ul',{'class': 'list-unstyled'})
    lq_li = ul.find_all('li')[1]
    download_link = lq_li.find('a')['href']
    download_link = 'http:' + download_link
    driver.get(download_link)
