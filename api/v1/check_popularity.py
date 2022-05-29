from fastapi import status, HTTPException, APIRouter
from pydantic import BaseModel, validator

from services.github_api import GithubApi
from utility.custom_renderer import CustomResponse


__all__ = ["check_popularity_router"]

check_popularity_router = APIRouter(prefix="/v1")


class RepoAddress(BaseModel):
    repo_address: str

    @validator("repo_address")
    def validate_repo_address(cls, v: str):
        if "http" not in v or "https" not in v or "/" not in v:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="the address you interned is not valid",
            )

        v = v.split("/")
        if len(v) < 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="the address you entered is not correct, it should contain owner/repo_name"
            )

        return "/".join(v[-2:])


@check_popularity_router.post(path="/check_popularity/", status_code=status.HTTP_200_OK)
@check_popularity_router.post(path="/check_popularity", status_code=status.HTTP_200_OK)
async def check_popularity(data: RepoAddress):
    result, message = await GithubApi.get_repo_popularity(repo_address=data.repo_address)
    return CustomResponse(content=result, message=message)
