import requests
from bs4 import BeautifulSoup
import re

KEYWORDS = ['python', 'игр', 'IT', 'разработк']
html_page = requests.get('https://habr.com/ru/all/').text


# Найдены ли ключевые слова в тексте
def keywords_found(text):
    for keyword in KEYWORDS:
        s = re.search(keyword, text, re.IGNORECASE)
        if s is not None:
            return True
        else:
            return False


soup = BeautifulSoup(html_page, 'html.parser')
articles = soup.find_all('article')

for article in articles:
    # Получить полный адрес статьи, затем всю статью в отдельный обьект
    article_href = 'https://habr.com' + article.find(class_='tm-article-snippet__title-link')['href']
    full_article = BeautifulSoup(requests.get(article_href).text, 'html.parser')
    full_article = full_article.find('article')
    # Ищем в превью и (Статья по ссылке может быть снята с публикации)
    if keywords_found(article.text) or keywords_found(full_article.text):
        date_string = article.find('time')['title']
        title_string = article.find('h2').a.span.text
        print(date_string, ' - ', title_string, ' - ', article_href)
