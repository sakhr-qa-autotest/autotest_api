from reqres.utils.base_session import BaseSession
from reqres.utils.settings import Settings


class Reqres:
    __session: BaseSession

    def __init__(self, setting: Settings):
        self.__session = BaseSession(url=setting.url())

    def session(self) -> BaseSession:
        return self.__session

    def get(self, url: str, **kwargs):
        return self.__session.get(url=url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.__session.post(url=url, data=data, json=json, **kwargs)
