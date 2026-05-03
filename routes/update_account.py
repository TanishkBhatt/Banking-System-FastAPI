from fastapi import APIRouter
from utils.schema import User
from utils.db_manager import access_users, import_data_to_db
from utils.hashing import hash_pin
from utils.schema import User
from pydantic import ValidationError

app = APIRouter(
    tags=["Account Management"]
)

@app.put("/update-account/{account_pin}/{updating_key}/{updated_value}")
def update_account(account_pin: str, updating_key: str, updated_value: str) -> dict:
    try:
        user_accounts: dict = access_users("database/accounts.json")
        hashed_pin = hash_pin(account_pin)

        if hashed_pin in user_accounts.keys():
            user = user_accounts[hashed_pin]
            user[updating_key] = updated_value
            try:
                User(
                    username=user["username"],
                    name=user["name"],
                    dob=user["dob"],
                    gender=user["gender"],
                    address=user["address"],
                    email=user["email"],
                    phone=user["phone"],
                    account_pin=account_pin,
                )
            except ValidationError as e:
                return {"message": "please use appropriate format"}
            else:
                user_accounts[hashed_pin] = user
                import_data_to_db("database/accounts.json", user_accounts)

                return {
                    "message": "account successfully updated",
                    "updating_key": updating_key,
                    "updated_value": updated_value,
                    "account_details": user_accounts[hashed_pin]
                }
        return {"message": "this account pin does not exists in our database."}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}