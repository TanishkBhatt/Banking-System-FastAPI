from fastapi import APIRouter
from models.db_manager import get_current_users

app = APIRouter()

@app.get("/get-all-users")
def get_all_users() -> dict:
    try:
        users_data = get_current_users("database/users.json")
        if users_data:
            for username, user_data in users_data.items():
                del user_data["account_pin"]
            return {
                "message": "data sucessfully recieved",
                "user_data": list(users_data.values())
                }
        return {"message": "the database in empty"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}