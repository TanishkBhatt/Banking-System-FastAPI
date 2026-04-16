from fastapi import APIRouter
from models.schema import User
from models.db_manager import get_current_users, import_data_to_db
from models.hashing import hash_pin

app = APIRouter(
    tags=["Account Management"]
)

@app.post("/create-account")
def create_account(data: User) -> dict:
    try:
        users: dict = get_current_users("database/users.json")
        invalid_pins: list = [user["account_pin"] for user in users.values()]
        invalid_usernames: list = [u_name for u_name in list(users.keys())]

        if data.account_pin not in invalid_pins:
            if data.username not in invalid_usernames:
                user_data = {
                    "name": str(data.name).title(),
                    "age": data.age,
                    "address": str(data.address).title(),
                    "email": data.email,
                    "account_pin": hash_pin(data.account_pin),
                    "balance": data.balance,
                    "loan": data.loan,
                    "gender": data.gender
                }
                users[data.username] = user_data
                import_data_to_db("database/users.json", users)

                del user_data["account_pin"]
                return {
                    "message": "account sucessfully created",
                    "account_details": {
                            data.username : user_data
                        }
                    }
            return {"message": "this username has been already taken"}
        return {"message": "this account pin has been already taken"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}