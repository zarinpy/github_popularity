import httpx
from setting import setting


class GithubApi:
    header = {
        "Content-Type": "application/vnd.api+json"
    }

    @classmethod
    async def get_repo(cls, repo_address: str):
        async with httpx.AsyncClient() as client:
            response = client.get(url=setting.GITHUB_API + repo_address, headers=cls.header)
            return response
