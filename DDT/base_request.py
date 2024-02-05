import requests


class BaseRequest:
    def __init__(self, base_url):
        if not base_url.endswith('/'):
            base_url += '/'
        self.base_url = base_url

    @staticmethod
    def _base_request(url, method, payload=None, is_json=False):

        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            if is_json:
                response = requests.post(url, json=payload)
            else:
                response = requests.post(url, data=payload)
        elif method == 'PUT':
            response = requests.put(url, data=payload)
        else:
            response = requests.delete(url)

        return response

    def get(self, route):
        url = self.base_url + route
        response = self._base_request(url, 'GET')
        return response

    def post(self, route, body):
        url = self.base_url + route
        response = self._base_request(url, 'POST', payload=body)
        return response.json()

    def put(self, route, body):
        url = self.base_url + route
        response = self._base_request(url, 'PUT', payload=body)
        return response.json()

    def delete(self, route):
        url = self.base_url + route
        response = self._base_request(url, 'DELETE')
        return response
