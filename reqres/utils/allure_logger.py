import json

import allure
from curlify import to_curl
from requests import Response


def allure_logger(func):
    def wrapper(*args, **kwargs):
        method, url = args[1], args[2]

        with allure.step(f"{method} {url}"):
            response: Response = func(*args, **kwargs)

            allure.attach(body=to_curl(response.request).encode('utf8'), name=f"Request: {response.status_code}",
                          attachment_type=allure.attachment_type.TEXT, extension='.txt')
            try:
                allure.attach(body=json.dumps(response.json(), indent=4), name=f"Response: {response.status_code}",
                              attachment_type=allure.attachment_type.JSON, extension='.json')
            except:
                allure.attach(body=response.text, name=f"Response: {response.status_code}",
                              attachment_type=allure.attachment_type.TEXT, extension='.txt')
            return response

    return wrapper
