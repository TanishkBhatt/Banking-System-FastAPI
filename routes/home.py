from fastapi import APIRouter, status
from schemas.home import ResponseModel

router = APIRouter(
    tags=["Home"]
)

@router.get(
    "/",
    response_model=ResponseModel,
    status_code=status.HTTP_200_OK
)
def route() -> dict[str, str]:
    return {"message": "Welcome to the home page!"}