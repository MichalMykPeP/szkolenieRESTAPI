import requests
from pytest_check import check

WRONG_PASSWORD = "wrong_password"  # stała


def test_wrong_pass(env_config, user_config):
    url: str = f"{env_config.url}/auth"
    # json: dict[str, str] = {"username": user_config.username, "password": str(user_config.password)} # to nie jest
    # potrzebne bo możemy użyć klasy z pydanitic jak user_config.model_dump() co jest poniżej
    json: dict[str, str] = {"username": user_config.username, "password": str(user_config.password) + "1"}
    # response: requests.Response = requests.post(url=url, json=user_config.model_dump())
    response: requests.Response = requests.post(url=url, json=json)
    with check:
        assert response.status_code == 200
    with check:
        assert "token" not in response.json()
    print(response.json())


def test_wrong_pass_model(env_config, user_config):
    url: str = f"{env_config.url}/auth"
    # json: dict[str, str] = {"username": user_config.username, "password": str(user_config.password)} # to nie jest
    # potrzebne bo możemy użyć klasy z pydanitic jak user_config.model_dump() co jest poniżej
    json: dict[str, str] = user_config.model_dump()
    json["password"] = "wrong_pass"
    response: requests.Response = requests.post(url=url, json=json)
    with check:
        assert response.status_code == 200
    with check:
        assert "token" not in response.json()
    print(response.json())


def test_only_user_exclude(env_config, user_config, auth_config):
    url: str = auth_config
    json: dict[str, str] = user_config.model_dump(exclude={"password"})  # exclude przyjmuje tylko sety
    response: requests.Response = requests.post(url=url, json=json)
    with check:
        assert response.status_code == 200
    with check:
        assert "token" not in response.json()
    print(response.json())


def test_only_user_include(env_config, user_config, auth_config):
    # url: str = f"{env_config.url}/auth"
    url: str = auth_config
    json: dict[str, str] = user_config.model_dump(include={"username"})  # include - tylko wybrane używa
    response: requests.Response = requests.post(url=url, json=json)
    with check:
        assert response.status_code == 200
    with check:
        assert "token" not in response.json()
    print(response.json())
