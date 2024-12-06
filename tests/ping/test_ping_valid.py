from http import HTTPStatus

import requests

# from pytest_check import check


def test_ping(ping_config):
    response: requests.Response = requests.get(url=ping_config)
    assert response.status_code == HTTPStatus.CREATED  # enumerator zamiast wpisania 201
