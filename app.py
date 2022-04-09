import json

def app(environ, start_response):
    response_data = {
        "name": "samuel adewale",
        "job": "developer",
        "message": "hello world"
    }
    data = bytes(json.dumps(response_data), 'utf-8')

    start_response("200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data)))
    ])

    return iter([data])