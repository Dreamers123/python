import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://thenewboston.com/search.php?type=1&sort=pop&page=' + str(page)
        source_code = requests.get("https://thenewboston.com/" + url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'class': 'user-name'}):
            href = link.get('href')
            title = link.string
            #print(href)
            #print(title)
            get_single_item_data(href)
        page +=1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class': 'profile - full - name'}):
        print(item_name.string)


trade_spider(1)