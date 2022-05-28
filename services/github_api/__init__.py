from setting import setting
from services import perform_request


class GithubApi:
    header = {
        "Content-Type": "application/vnd.api+json"
    }

    @classmethod
    async def get_repo(cls, repo_address: str):
        response = await perform_request(url=setting.GITHUB_API + repo_address, method="get", headers=cls.header)
        return response
