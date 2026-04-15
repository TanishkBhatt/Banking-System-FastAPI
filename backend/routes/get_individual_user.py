from fastapi import APIRouter
from models.db_manager import get_current_users
from models.hashing import verify

app = APIRouter(
     tags=["Current Users"]
)

@app.get("/get-indvidual-user/{account_pin}")
def get_indvidual_user(account_pin: str) -> dict:
    try:
        users: dict = get_current_users("database/users.json")
        for username, user_data in users.items():
            if verify(user_data["account_pin"], account_pin):
                del user_data["account_pin"]
                return {
                    "message": "data sucessfully recieved",
                    "user_data": {username: user_data}
                    }
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}