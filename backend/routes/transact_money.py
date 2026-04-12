from fastapi import APIRouter
from models.db_manager import get_current_users, import_data_to_db
from models.hashing import hash_pin, verify

app = APIRouter()

@app.put("/transact-money/{account_pin}/{money_to_transact}")
def transact_money(account_pin: str, money_to_transact: float) -> dict:
    try:
        users: dict = get_current_users("database/users.json")
        for user, user_data in users.items():
            if verify(user_data["account_pin"], account_pin):
                if user_data["balance"] >= money_to_transact:
                    user_data["balance"] -= money_to_transact

                    import_data_to_db("database/users.json", users)
                    del user_data["account_pin"]

                    return {
                        "message": "money sucessfully transacted",
                        "transacted_money": money_to_transact,
                        "account_details": {
                                user: user_data
                            }
                        }
                else:
                    return {"messange": "invalid request, user can't transact money more than its balance"}
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}