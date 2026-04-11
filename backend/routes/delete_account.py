from fastapi import APIRouter
from models.db_manager import get_current_users, import_data_to_db

app = APIRouter()

@app.delete("/delete-account/{account_pin}")
def delete_account(account_pin: str) -> dict:
    try:
        users: dict = get_current_users("database/users.json")

        for username, user_data in users.items():
            if user_data["account_pin"] == account_pin:
                deleted_account_username = username
                deleted_account_details = user_data
                del users[username]

                import_data_to_db("database/users.json", users)
                return {
                    "message": "account sucessfully deleted",
                    "deleted_account_details": {
                        deleted_account_username: deleted_account_details
                    }
                }
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": "something went wrong",
                "error": str(e)}