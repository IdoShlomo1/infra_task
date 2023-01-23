import pytest
from settings import API_URL
from framework import RestClient
from framework.api import Session


@pytest.fixture
def api_client() -> RestClient:
    return RestClient(Session(), API_URL)
