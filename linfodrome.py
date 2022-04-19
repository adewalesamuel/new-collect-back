import json
from crawler import Crawler
from bs4 import NavigableString
import re

def write_file(content):
    with open('text.txt', "w", encoding='utf-8') as file:
        file.write(str(content))

class Linfodrome(Crawler):
    def __init__(self):
        self.HOST = "https://www.linfodrome.com"
        self.ARTICLES_ENDPOINT = "/"
        self.ARTICLES_CONTAINER_CLASS = "content"
        self.url = self.HOST + self.ARTICLES_ENDPOINT
        self.articles = list()

        super().__init__(self.url)

    def get_articles(self) -> list:

        for a in self.soup.find_all("li", class_=self.ARTICLES_CONTAINER_CLASS):
            self.articles.append({
                "title": self.get_article_title(a).replace("\xa0", ""),
                "date": self.get_article_date(a),
                "img_url": self.get_article_img_url(a),
                "href": self.HOST + self.get_article_url(a)
            })
        
        return self.articles[:15]

    def get_article_title(self, article: NavigableString, is_display=False) -> str:
        return article.find("a", class_="in-link-inherit").get_text()

    def get_article_date(self, article: NavigableString, is_display=False) -> str:
        span = article.find("span", class_="date uk-margin-small-right")

        if span is not None:
            return span.time.get_text()

    def get_article_img_url(self, article: NavigableString, is_display=False) -> str:
        img = article.find("img", class_="image")

        if img is not None:
            return img.attrs['data-src']

    def get_article_url(self, article: NavigableString, is_display=False) -> str:
        return article.find("a", class_="in-link-inherit").attrs['href']
