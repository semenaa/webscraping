import requests
from bs4 import BeautifulSoup
import re

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'корпорац', 'разработк']
html_page = requests.get('https://habr.com/ru/all/').text
result = []


def keywords_found(text):
    for keyword in KEYWORDS:
        return re.match(keyword, text)


soup = BeautifulSoup(html_page, 'html.parser')
articles = soup.find_all('article')

for article in articles:
    article_preview = article.find(class_='article-formatted-body')
    pass
    if keywords_found(article_preview):
        date_string = article.find('time').title
        name_string = article.find('h2').a.span.text
