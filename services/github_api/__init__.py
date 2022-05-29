from setting import setting
from services import perform_request
from fastapi import HTTPException, status


class GithubApi:
    header = {
        "Content-Type": "application/vnd.api+json"
    }

    @classmethod
    async def get_repo_popularity(cls, repo_address: str):
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

        if score >= 500:
            message = f"the {repo_address[1]} repo is popular"
            result = {"starts": stars, "forks": forks}
        else:
            message = f"the {repo_address[1]} repo is not popular"
            result = {"starts": stars, "forks": forks}
        return result, message
