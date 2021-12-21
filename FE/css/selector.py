import requests
from bs4 import BeautifulSoup

def crawling_template(url, css_selector):
    return_data = list()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    datasl = soup.select(css_selector)
    for item in datasl:
        return_data.append(item.get_text())
    return return_data

res = crawling_template('https://github.com/jiheenim27', 'span[class*=repo]')

for i in res:
    print(i)