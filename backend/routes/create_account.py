from fastapi import APIRouter
from models.schema import User
from models.db_manager import get_current_users, import_data_to_db

app = APIRouter()

@app.post("/create-account")
def create_account(data: User) -> dict:
    try:
        users: dict = get_current_users("database/users.json")
        invalid_pins: list = [user["account_pin"] for user in users.values()]
        invalid_usernames: list = [u_name for u_name in list(users.keys())]

        if data.account_pin not in invalid_pins:
            if data.username not in invalid_usernames:
                user_data = {
                    "name": data.name,
                    "age": data.age,
                    "address": data.address,
                    "email": data.email,
                    "account_pin": data.account_pin,
                    "balance": data.balance
                }
                users[data.username] = user_data
                import_data_to_db("database/users.json", users)
                return {
                    "message": "account sucessfully created",
                    "account_details": {
                            data.username : user_data
                        }
                    }
            return {"message": "this username has been already taken"}
        return {"message": "this account pin has been already taken"}
    except Exception as e:
        return {"message": "something went wrong",
                "error": str(e)}