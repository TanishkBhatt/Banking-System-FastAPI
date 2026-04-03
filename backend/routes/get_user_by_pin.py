from fastapi import APIRouter
from models.utils import get_current_users

app = APIRouter()

@app.get("/get-user-by-pin")
def get_user_by_pin(account_pin: str) -> dict:
    users = get_current_users("database/users.json")
    for key, user in users.items():
        if user["account_pin"] == account_pin:
            data = users[key]
            return data
    return {"message": "invalid account pin"}