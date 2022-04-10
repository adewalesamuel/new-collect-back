import json
from crawler import Crawler
from bs4 import NavigableString
import re

class AbidjanNet(Crawler):
    def __init__(self):
        self.HOST = "https://news.abidjan.net"
        self.ARTICLES_ENDPOINT = "/"
        self.ARTICLES_CONTAINER_CLASS = "grd-item ebloc-big"
        self.DISPLAY_ARTICLE_CONTAINER_CLASS = "grd-item ebloc-mea"
        self.url = self.HOST + self.ARTICLES_ENDPOINT
        self.articles = list()

        super().__init__(self.url)

    def get_articles(self) -> list:
        da = self.soup.find("a", class_=self.DISPLAY_ARTICLE_CONTAINER_CLASS)
        self.articles.append({
            "title": self.get_article_title(da, True),
            "date": self.get_article_date(da, True),
            "img_url": self.get_img_url_from_style(self.get_article_img_url(da, True)),
            "href": self.HOST + self.get_article_url(da, True)
        })
        
        for a in self.soup.find_all("a", class_=self.ARTICLES_CONTAINER_CLASS):
            self.articles.append({
                "title": self.get_article_title(a),
                "date": self.get_article_date(a),
                "img_url": self.get_article_img_url(a),
                "href": self.get_article_url(a)
            })
        
        return self.articles

    
    def get_true_date(self, raw_date: str):
        return raw_date.split(" - ")[1].strip()

    def get_img_url_from_style(self, style: str):
        return re.search("url\(\'(.*?)\'\)", style).group(1)

    def get_article_title(self, article: NavigableString, is_display=False) -> str:
        if is_display is True:
            return article.div.contents[3].get_text()

        return article.contents[3].get_text()

    def get_article_date(self, article: NavigableString, is_display=False) -> str:
        if is_display is True:
            return self.get_true_date(article.div.contents[1].get_text())

        return self.get_true_date(article.span.get_text())

    def get_article_img_url(self, article: NavigableString, is_display=False) -> str:
        if is_display is True:
            return article.picture.attrs['style']
    
        return article.picture.img.attrs['data-original']

    def get_article_url(self, article: NavigableString, is_display=False) -> str:
        return article.attrs['href']