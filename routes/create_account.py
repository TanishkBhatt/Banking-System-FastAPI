from fastapi import APIRouter
from utils.schema import User
from utils.db_manager import access_users, import_data_to_db
from utils.hashing import hash_pin, verify
from utils.age_calc import age_calc

app = APIRouter(
    tags=["Account Management"]
)

@app.post("/create-account")
def create_account(data: User) -> dict:
    try:
        user_accounts: dict = access_users("database/accounts.json")
        users_history: dict = access_users("database/user_history.json")
        invalid_pins: list = [verify(pin, data.account_pin) for pin in user_accounts.keys()]
        invalid_usernames: list = [u_data["username"] for u_data in user_accounts.values()]

        if not any(invalid_pins):
            if data.username not in invalid_usernames:
                age = age_calc(data.dob)
                if age >= 18:
                    user_data = {
                        "username": data.username,
                        "name": data.name.title(),
                        "dob": str(data.dob),
                        "gender": data.gender,
                        "address": data.address.title(),
                        "email": data.email,
                        "phone": data.phone,
                        "balance": 0.0,
                        "loan": 0.0
                    }
                    user_history = {
                            "transaction_history": [],
                            "loan_history": []
                        }

                    user_accounts[hash_pin(data.account_pin)] = user_data
                    import_data_to_db("database/accounts.json", user_accounts)

                    users_history[hash_pin(data.account_pin)] = user_history
                    import_data_to_db("database/user_history.json", users_history)

                    return {
                        "message": "account successfully created",
                        "account_details": user_data
                        }

                return {"message": "you are under 18, you can't create an account"}
            return {"message": "this username has been already taken"}
        return {"message": "this account pin has been already taken"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}