from crawler import Crawler
from bs4 import NavigableString
import re

class Koaci(Crawler):
    def __init__(self):
        self.HOST = "https://www.koaci.com"
        self.ARTICLES_ENDPOINT = "/"
        self.ARTICLES_CONTAINER_CLASS = "slide"
        self.url = self.HOST + self.ARTICLES_ENDPOINT
        self.articles = list()

        super().__init__(self.url)

    def get_articles(self) -> list:       
        print("koaci") 
        for a in self.soup.find_all("div", class_=self.ARTICLES_CONTAINER_CLASS):
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
        return article.contents[1].contents[1].contents[1].contents[0].get_text().split("\xa0\n")[1].replace('\t', '').replace('\n','')

    def get_article_date(self, article: NavigableString, is_display=False) -> str:
        return ""
    
    def get_article_url(self, article: NavigableString) -> str:
        return article.contents[1].a.attrs['href']

    def get_article_img_url(slef, article: NavigableString, is_display=False) -> str:
        return article.contents[3].img.attrs['src']