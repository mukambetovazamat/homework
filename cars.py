import requests
from bs4 import BeautifulSoup

URL = 'https://cars.kg/offers/?vendor=57fa24ee2860c45a2a2c093b'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36', 'accept': '*/*',}

def get_html(url,params=None):
    r = requests.get(url,headers= HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('a', class_='catalog-list-item')
    cars = []
    
    for item in items:
        cars.append({
            'title': item.find('span',class_='catalog-item-caption').get_text()
        })

    # print (items)
    print(cars)
def pars_cars():
    html = get_html(URL)
    if html.status_code == 200:
        print(html.text)
    else:
        print('eror')    

    

pars_cars()