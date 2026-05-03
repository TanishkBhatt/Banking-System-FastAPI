from fastapi import APIRouter
from utils.db_manager import access_users

app = APIRouter(
     tags=["Current Users"]
)

@app.get("/get-all-users")
def get_all_users() -> dict:
    try:
        users_data = access_users("database/accounts.json")
        if users_data:
            return {
                "message": "data sucessfully recieved",
                "user_data": list(users_data.values())
                }
        return {"message": "the database is empty"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}