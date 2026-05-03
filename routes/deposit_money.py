from fastapi import APIRouter
from utils.db_manager import access_users, import_data_to_db
from utils.hashing import verify
from datetime import datetime

app = APIRouter(
    tags=["Money Management"]
)

@app.put("/deposit-money/{account_pin}/{money_to_deposit}")
def deposit_money(account_pin: str, money_to_deposit: float) -> dict:
    try:
        user_accounts: dict = access_users("database/accounts.json")
        users_history: dict = access_users("database/user_history.json")

        for pin, user_data in user_accounts.items():
            if verify(pin, account_pin):
                user_data["balance"] += money_to_deposit

                for user_pin, history in users_history.items():
                    if verify(user_pin, account_pin):
                        users_history[user_pin]["transaction_history"].append(
                            {   
                                "status": "deposit",
                                "money": money_to_deposit,
                                "datetime": str(datetime.today().strftime("%d/%m/%Y, %H:%M:%S"))
                            }
                        )
                    
                        import_data_to_db("database/accounts.json", user_accounts)
                        import_data_to_db("database/user_history.json", users_history)
                        
                        return {
                                "message": "money sucessfully deposited",
                                "deposited_money": money_to_deposit,
                                "account_details": user_data,
                                "account_history": history["transaction_history"]
                            }
                return {"message": "error - user history not found"}
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}