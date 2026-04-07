from fastapi import APIRouter
from models.db_manager import get_current_users

app = APIRouter()

@app.get("/get-user-by-pin/{account_pin}")
def get_user_by_pin(account_pin: str) -> dict:
    users: dict = get_current_users("database/users.json")
    for username, user_data in users.items():
        if user_data["account_pin"] == account_pin:
            data = {username: users[username]}
            return {
                "message": "data sucessfully recieved",
                "data": data
                }
    return {"message": "invalid account pin"}