from fastapi import APIRouter, status
from github_api import GithubApi

from pydantic import BaseModel, HttpUrl


__all__ = ["check_popularity_router"]

check_popularity_router = APIRouter(prefix="/check_popularity")


class RepoAddress(BaseModel):
    repo_address: HttpUrl


@check_popularity_router.post(path="/", status_code=status.HTTP_200_OK)
async def check_popularity(data: RepoAddress):
    response = await GithubApi.get_repo(addr=data.repo_address)
    return response
