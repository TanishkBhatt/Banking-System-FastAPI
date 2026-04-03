from fastapi import APIRouter
from models.utils import get_current_users

app = APIRouter()

@app.get("/get-all-users")
def get_all_users() -> dict:
    users_data = get_current_users("database/users.json")
    return {
        "message": "data sucessfully recieved",
        "data": users_data
        }