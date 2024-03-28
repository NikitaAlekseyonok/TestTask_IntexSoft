import pytest
from helpers.logger_helper import Logger


@pytest.fixture(scope="session")
def api_tests():
    Logger.info(f"Start API tests")

    yield

    Logger.info(f"End API tests")