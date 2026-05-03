from fastapi import APIRouter

app = APIRouter(
    tags=["Home"]
)

@app.get("/")
def home() -> dict:
    return {"message": "welcome to banking management system"}