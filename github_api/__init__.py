import httpx
from setting import setting


class GithubApi:
    header = {
        "Content-Type": "application/vnd.api+json"
    }

    @classmethod
    async def get_repo(cls, addr: str):
        async with httpx.AsyncClient() as client:
            response = client.get(url=addr, headers=cls.header)
