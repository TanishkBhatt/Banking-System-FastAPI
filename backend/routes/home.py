from fastapi import APIRouter

app = APIRouter()

@app.get("/")
def home() -> dict:
    return {"message": "welcome to banking management system"}