import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/1960_Copa_Libertadores"

res = requests.get(URL).text
soup = BeautifulSoup(res,'xml')
for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
    data = items.find_all(['th','td'])
    try:
        country = data[0].a.text
        title = data[1].a.text
        name = data[1].a.find_next_sibling().text
    except IndexError:pass
    print("{}|{}|{}".format(country,title,name))