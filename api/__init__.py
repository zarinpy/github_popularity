from fastapi import APIRouter
from api.v1 import check_popularity_router


__all__ = ["api"]
api = APIRouter()

# add whatever api you creating
api.include_router(check_popularity_router, tags=['github'])
