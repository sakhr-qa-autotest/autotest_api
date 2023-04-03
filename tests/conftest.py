import pytest

from reqres.utils.reqres import Reqres
from reqres.utils.settings import Settings


def pytest_addoption(parser):
    parser.addoption("--env", default="test")


@pytest.fixture(scope='session')
def settings(request) -> Settings:
    setting = Settings(request.config.getoption("--env"))

    return setting


@pytest.fixture(scope='session')
def reqres(settings):
    return Reqres(settings)
