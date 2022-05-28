from fastapi import APIRouter, status
from services.github_api import GithubApi

from pydantic import BaseModel, HttpUrl
from utility.custom_renderer import CustomResponse


__all__ = ["check_popularity_router"]

check_popularity_router = APIRouter(prefix="/check_popularity")


class RepoAddress(BaseModel):
    repo_address: HttpUrl


@check_popularity_router.post(path="/", status_code=status.HTTP_200_OK)
async def check_popularity(data: RepoAddress):
    result, message = await GithubApi.get_repo_popularity(repo_address=data.repo_address)
    return CustomResponse(content=result, message=message)
