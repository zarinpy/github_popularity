import os

from pydantic import BaseSettings

__all__ = ["setting"]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file = f"{BASE_DIR}/.env"


class Setting(BaseSettings):
    GITHUB_API: str

    class Config:
        env_file = env_file


setting = Setting()
