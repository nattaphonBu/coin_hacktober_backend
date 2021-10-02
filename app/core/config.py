from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str
    APP_NAME: str = "COIN_HACKTOBER_BACKEND"
    ADMIN_EMAIL: str = "nat@sennalabs.com"
    # ITEMS_PER_USER: int = 50
    # DB_USER: str
    # DB_PASSWORD: str
    # DB_HOST: str
    # DB_PORT: int
    # DB_NAME: str
    # DB_DRIVER: str
    # SQL_DRIVER: str

    class Config:
        env_file = "./app/.env"


settings = Settings()
