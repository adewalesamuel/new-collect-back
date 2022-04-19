import json
from pprint import pprint
from abidjan_net import AbidjanNet
from koaci import Koaci
from linfodrome import Linfodrome

def app(environ, start_response):
    data = list()

    try:
        if environ['PATH_INFO'] == '/abidjan_net':
            abidjan_net = AbidjanNet()
            articles = abidjan_net.get_articles()
            data = bytes(json.dumps(articles), 'utf-8')

        if environ['PATH_INFO'] == '/koaci':
            koaci = Koaci()
            articles = koaci.get_articles()
            data = bytes(json.dumps(articles), 'utf-8')
       
        if environ['PATH_INFO'] == '/linfodrome':
            linfodrome = Linfodrome()
            articles = linfodrome.get_articles()
            data = bytes(json.dumps(articles), 'utf-8')

        start_response("200 OK", [
            ("Content-Type", "application/json"),
            ("Content-Length", str(len(data)))
        ])
    except:
        data = bytes(json.dumps({
            "error": True,
            "message": "Erreur de connexion !"
        }), 'utf-8')

        start_response("500 Internal Server Error", [
            ("Content-Type", "application/json"),
            ("Content-Length", str(len(data))),
        ])

    return iter([data])