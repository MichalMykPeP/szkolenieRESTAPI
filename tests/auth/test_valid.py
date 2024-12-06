from http import HTTPStatus

import requests
from pytest_check import check


def test_valid(env_config, user_config, auth_config):
    response: requests.Response = requests.post(url=auth_config, json=user_config.model_dump())
    with check:
        assert response.status_code == 200
    with check:
        assert response.status_code == HTTPStatus.OK  # enumerator zamiast wpisania 200
    with check:
        assert "token" in response.json()
    print(response.json())


def test_extra_field(env_config, user_config):
    url: str = f"{env_config.url}/auth"
    # json: dict[str, str] = {"username": user_config.username, "password": str(user_config.password)} # to nie jest
    # potrzebne bo możemy użyć klasy z pydanitic jak user_config.model_dump() co jest poniżej
    json: dict[str, str] = user_config.model_dump()
    json["extra"] = "value"
    response: requests.Response = requests.post(url=url, json=json)
    with check:
        assert response.status_code == 200
    with check:
        assert "token" in response.json()
    print(response.json())
