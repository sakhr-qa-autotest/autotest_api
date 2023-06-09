import logging

from curlify import to_curl
from requests import Session, Response
from reqres.utils.allure_logger import allure_logger

def request_logger(func):
    def wrapper(*args, **kwargs):
        response: Response = func(*args, **kwargs)
        logging.info(f"- code: {response.status_code} - {to_curl(response.request)}")

        return response

    return wrapper


class BaseSession(Session):
    def __init__(self, url):
        super(BaseSession, self).__init__()
        self.url = url

    @allure_logger
    @request_logger
    def request(self, method, url, **kwargs) -> Response:
        response = super().request(method, self.url + url, **kwargs)
        return response
