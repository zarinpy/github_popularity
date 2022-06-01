import base64

from fastapi import HTTPException

from services import perform_request
from setting import setting


class GithubApi:
    header = {
        "Content-Type": "application/vnd.api+json"
    }

    @classmethod
    async def get_repo_popularity(cls, repo_address: str):
        user_pass = f"{setting.USERNAME}:{setting.ACCESS_TOKEN}".encode()
        token = base64.b64encode(user_pass)
        cls.header["Authorization"] = f"Basic {token.decode()}"
        url = setting.GITHUB_API + "/repos/" + repo_address
        response, status_code = await perform_request(url=url, method="get", headers=cls.header)

        if status_code != 200:
            message = response["message"]
            raise HTTPException(status_code=status_code, detail=message)

        if "forks_count" not in response or repo_address.split("/")[1] != response["name"]:
            repo_name = repo_address.split("/")[1]
            raise HTTPException(
                status_code=status_code,
                detail=f"this address is not for {repo_name}, we couldn't find the name",
            )

        forks = response["forks_count"]
        stars = response["stargazers_count"]
        score = stars * 1 + forks * 2

        repo_name = repo_address.split("/")[1]
        if score >= 500:

            message = f"the {repo_name} repo is popular"
            result = {"starts": stars, "forks": forks}
        else:
            message = f"the {repo_name} repo is not popular"
            result = {"starts": stars, "forks": forks}
        return result, message
