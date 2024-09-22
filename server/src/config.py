from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    origins: str = Field(alias="CORS_ORIGINS")
    host: str
    port: int
    reload: bool = Field(alias="SERVER_RELOAD")
