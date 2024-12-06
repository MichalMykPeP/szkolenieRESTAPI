# from src.configs import EnvConfig, UserConfig
import pytest


@pytest.fixture(scope="session")
def booking_config(env_config) -> str:
    """booking endpoint"""
    return f"{env_config.url}/booking"
