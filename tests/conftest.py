import pytest
import requests

from src.configs import EnvConfig
from src.configs import UserConfig


@pytest.fixture(scope="session")
def env_config() -> EnvConfig:
    """Environment variables (like url)"""
    return EnvConfig()


@pytest.fixture(scope="session")
def user_config() -> UserConfig:
    """Username and password for authentication"""
    return UserConfig()


@pytest.fixture(scope="module")
def token(env_config, user_config) -> str | None:  # funkcja zwraca string albo None
    response: requests.Response = requests.post(url=f"{env_config.url}/auth", json=user_config.model_dump())
    if response.status_code != 200:  # jak odpowiedź nie jest 200 to nie zwraca tokena i daje None
        return None

    if "token" not in response.json():  # jak nie ma tokena w odpowiedzi to zwraca None
        return None

    return response.json()["token"]  # zwraca wartość tokena

    #  dokłanie to samo co powyżej
    #  return response.json()["token"] if response.status_code == 200 and "token" in response.json() else None
