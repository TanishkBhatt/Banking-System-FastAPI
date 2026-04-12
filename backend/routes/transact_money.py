from fastapi import APIRouter
from models.db_manager import get_current_users, import_data_to_db

app = APIRouter()

@app.put("/transact-money/{account_pin}/{money_to_transact}")
def transact_money(account_pin: str, money_to_transact: float) -> dict:
    try:
        users: dict = get_current_users("database/users.json")
        for user, user_data in users.items():
            if user_data["account_pin"] == account_pin:
                if user_data["balance"] >= money_to_transact:
                    user_data["balance"] -= money_to_transact

                    import_data_to_db("database/users.json", users)
                    return {
                        "message": "money sucessfully transacted",
                        "transacted_money": money_to_transact,
                        "account_details": {
                                user: user_data
                            }
                        }
                else:
                    return {"messange": "invalid request, user can't transact money more than its balance"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}