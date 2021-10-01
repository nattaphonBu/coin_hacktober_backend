from typing import Optional
from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("get-name")
def read_root(name):
    return {f"Hello": "{name}"}