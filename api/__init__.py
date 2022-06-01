from fastapi import APIRouter

from api.v1 import check_popularity_router


__all__ = ["root_api"]
root_api = APIRouter()

# add whatever api you creating
root_api.include_router(check_popularity_router, tags=['github'])
