from fastapi import APIRouter

from app.api.endpoints.stater import hello

api_router = APIRouter()
api_router.include_router(hello.router, tags=["starter"])
