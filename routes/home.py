from fastapi import APIRouter, status
from schemas.home import HomeResponse

router = APIRouter(
    tags=["Home"]
)

@router.get(
    "/",
    response_model=HomeResponse,
    status_code=status.HTTP_200_OK
)
def home() -> dict[str, str]:
    return {"message": "Welcome to the home page!"}