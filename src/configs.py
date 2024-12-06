import pydantic_settings

# from pydantic import SecretStr


class UserConfig(pydantic_settings.BaseSettings):
    # env_prefix ustawia prefix z pliku .env (nie trzeba pisać przy definicji),
    # frozen nie pozwala na modyfikacje zmiennych, extra ignoruje dodatkowe zmienne
    model_config = pydantic_settings.SettingsConfigDict(env_prefix="QA_", frozen=True, env_file=".env", extra="ignore")

    username: str = ""
    password: str = ""

    # @field_serializer( field: "password", when_used="json")
    # def dump_secret(self, v):
    #     return v.get_secret_value()


class EnvConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_ENV_", frozen=True, env_file=".env", extra="ignore"
    )

    url: str = ""
