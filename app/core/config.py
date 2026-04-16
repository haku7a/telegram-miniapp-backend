from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: str

    DB_HOST: str
    DB_PORT: int

    BOT_TOKEN: SecretStr

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD.get_secret_value()}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
