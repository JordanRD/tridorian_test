import requests


class APIClient:
    def __init__(self, base_url: str, headers: dict = {}, params: dict | None = None):
        self.base_url = base_url.rstrip("/")
        self.headers = headers
        self.params = params

    def request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.request(
            method,
            url,
            headers={**self.headers, **kwargs.pop("headers", {})},
            params={**self.params, **kwargs.pop("params", {})},
            **kwargs,
        ) 
        response.raise_for_status()
        return response

    def get(self, endpoint: str, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)
