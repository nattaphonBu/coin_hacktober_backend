from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def hello():
    return {"Hello": "World"}


@router.post("get-name")
def get_name(name):
    return {f"Hello": "{name}"}
