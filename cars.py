import requests
from bs4 import BeautifulSoup

URL = 'https://cars.kg/offers/?vendor=57fa24ee2860c45a2a2c093b'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36', 'accept': '*/*',}
LINK = 'https://cars.kg'

def get_html(url,params=None):
    r = requests.get(url,headers= HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('a', class_='catalog-list-item')
    
    cars = []
    
    for item in items:    #catalog-list-item      catalog-item-params  catalog-item-descr
        cars.append({
            'title': item.find('span',class_='catalog-item-caption').get_text(strip=True).replace('\n', "").replace('\xa0', ""),
            'description': item.find('span',class_='catalog-item-descr').get_text(strip=True).replace('\n', "").replace('\xa0', ""),
            'link': item.find('span',class_='catalog-item-params').get_text(strip=True).replace('\n\n', "").replace('\xa0', ""),
            
            'image': LINK+ item.find('img',class_='catalog-item-cover-img').get('src').replace('\n\n', "").replace('\xa0', ""),
            'year': item.find('span',class_="caption-year").get_text(strip=True).replace('\n\n', "").replace('\xa0', ""),
            'km': item.find('span',class_='catalog-item-mileage').get_text(strip=True).replace('\n\n', "").replace('\xa0', ""),
            'price':item.find('span',class_='catalog-item-price').get_text()

        })

    print (cars)
    
    # print(lcars))
    
def pars_cars():
    html = get_html(URL)
    if html.status_code == 200:
        # print(html.text)
        get_content(html.text)
    else:
        print('eror')    

    

pars_cars()
