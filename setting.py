import os

from pydantic import BaseSettings

__all__ = ["setting"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_file = f"{BASE_DIR}/.env"


class Setting(BaseSettings):
    HOST: str
    GENERAL_URL_PORT: int
    DOC_URL: str

    GITHUB_API: str

    class Config:
        env_file = env_file


setting = Setting()
