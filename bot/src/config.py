from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    RABBIT_HOST: str
    RABBIT_PORT: int
    RABBIT_USER: str
    RABBIT_PASS: str

    BOT_TOKEN: str

    @property
    def RABBIT_URL(self):
        return f"amqp://{self.RABBIT_USER}:{self.RABBIT_PASS}@{self.RABBIT_HOST}:{self.RABBIT_PORT}/"


settings = Settings()
