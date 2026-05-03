from fastapi import APIRouter
from utils.db_manager import access_users, import_data_to_db
from utils.hashing import verify
from datetime import datetime

app = APIRouter(
    tags=["Money Management"]
)

@app.put("/withdraw-money/{account_pin}/{money_to_withdraw}")
def withdraw_money(account_pin: str, money_to_withdraw: float) -> dict:
    try:
        user_accounts: dict = access_users("database/accounts.json")
        users_history: dict = access_users("database/user_history.json")

        for pin, user_data in user_accounts.items():
            if verify(pin, account_pin):
                if user_data["balance"] >= money_to_withdraw:
                    user_data["balance"] -= money_to_withdraw

                    for user_pin, history in users_history.items():
                        if verify(user_pin, account_pin):
                            users_history[user_pin]["transaction_history"].append(
                                {   
                                    "status": "withdraw",
                                    "money": money_to_withdraw,
                                    "datetime": str(datetime.today().strftime("%d/%m/%Y, %H:%M:%S"))
                                }
                            )

                            import_data_to_db("database/accounts.json", user_accounts)
                            import_data_to_db("database/user_history.json", users_history)

                            return {
                                    "message": "money sucessfully withdrawal",
                                    "withdrawal_money": money_to_withdraw,
                                    "account_details": user_data,
                                    "account_history": history["transaction_history"]
                                }
                    return {"message": "error - user history not found"}
                return {"message": "user can't transact money more than your balance"}
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}