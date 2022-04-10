import json
from os import truncate
from abidjan_net import AbidjanNet

def app(environ, start_response):
    data = list()

    try:
        if environ['PATH_INFO'] == '/abidjan_net':
            abidjan_net = AbidjanNet()
            articles = abidjan_net.get_articles()
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