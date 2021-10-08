from fastapi import APIRouter

from app.api.endpoints.stater import hello
from app.api.endpoints.binance_api import binance_api

api_router = APIRouter()

api_router.include_router(hello.router, tags=["starter"])
api_router.include_router(binance_api.router, tags=["get-coin-price"])
