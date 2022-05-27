from fastapi import APIRouter, status, Request

from pydantic import BaseModel, HttpUrl


__all__ = ["auth_router"]

auth_router = APIRouter(prefix="/check_popularity")


class RepoAddress(BaseModel):
    url: str = HttpUrl


@auth_router.post(path="/", status_code=status.HTTP_200_OK)
async def check_popularity(
        request: Request,
):
    pass