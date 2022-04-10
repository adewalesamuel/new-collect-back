from urllib.request import urlopen
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, url: str):
        if (url is not None) : self.url = url

        self.site_content = b''
        self.soup = None
        self.error = None
        self.error_message = ""

        self.init()
    
    def get_site_content(self):
        with urlopen(self.url) as request:
            if request.code == 200:
                self.site_content = request.read()
            else:
                self.error = True
                self.error_message = "Could not get site content"
        
    def init(self):
        self.get_site_content()

        if (self.error is not True):
            self.soup = BeautifulSoup(self.site_content, 'html.parser')

