from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from fastapi_pagination import add_pagination

from app.api.api import api_router
from app.core.config import settings

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

# add_pagination(app)
