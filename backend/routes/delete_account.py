from fastapi import APIRouter
from models.utils import get_current_users, import_data_to_db

app = APIRouter()

@app.delete("/delete-account")
def delete_account(account_pin: str) -> dict:
    users = get_current_users("database/users.json")

    for key, user in users.items():
        if user["account_pin"] == account_pin:
            deleted_account_username = key
            deleted_account_details = user
            del users[key]

            import_data_to_db("database/users.json", users)
            return {
                "message": "account sucessfully deleted",
                "deleted_account_details": {
                    deleted_account_username: deleted_account_details
                }
            }
    return {"message": "invalid account pin"}