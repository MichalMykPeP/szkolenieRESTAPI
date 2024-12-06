# from src.configs import EnvConfig, UserConfig
import pytest


@pytest.fixture(scope="session")
def ping_config(env_config) -> str:
    """auth endpoint"""
    return f"{env_config.url}/ping"
