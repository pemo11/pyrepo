# class-Attribut abfragen with BeautifulSoup
from bs4 import BeautifulSoup

html = "<td class='val1'/><td col='1'/><td class='val2' />"

bsoup = BeautifulSoup(html, 'html.parser')

for td in bsoup.find_all('td'):
    if td.has_attr('class'):
        print(td['class'][0])

for td in bsoup.find_all('td',class_='val2'):
    print(td['class'][0])