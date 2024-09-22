from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Config(BaseSettings):
    db_host: str
