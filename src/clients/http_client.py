import requests
import json
constant_headers = {'Content-type': 'application/json'}

def get(url, query_params = None, headers = None):
    response = requests.get(url, params=query_params, headers=__get_headers(headers))
    return response.json()

def post(url, body, headers = None):
    body = json.dumps(body)
    response = requests.post(url, data=body, headers=__get_headers(headers))
    return response.json()

def put(url, body, headers = None):
    body = json.dumps(body)
    response = requests.put(url, data=body, headers=__get_headers(headers))
    return response.json()

def patch(url, body, headers = None):
    body = json.dumps(body)
    response = requests.patch(url, data=body, headers=__get_headers(headers))
    return response.json()

def __get_headers(headers):
    heads = constant_headers
    if headers:
        for key, value in headers.items():
            heads[key] = value
    return heads

