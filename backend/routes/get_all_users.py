from fastapi import APIRouter
from models.db_manager import get_current_users

app = APIRouter()

@app.get("/get-all-users")
def get_all_users() -> dict:
    try:
        users_data = get_current_users("database/users.json")
        if users_data:
            return {
                "message": "data sucessfully recieved",
                "data": users_data
                }
        return {"message": "database in empty"}
    except Exception as e:
        return {"message": "something went wrong",
                "error": str(e)}