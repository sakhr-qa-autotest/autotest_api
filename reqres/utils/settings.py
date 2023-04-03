import json

from reqres.utils.file import abs_path_from_project


class Settings:
    __url: str

    def __init__(self, env: str):
        try:
            fp = open(abs_path_from_project(f'../config.{env}.json'))
            config = json.loads(fp.read())

            if 'url' in config:
                self.__url = config['url']
        except:
            raise Exception("Environment file not found")

    def url(self):
        return self.__url
