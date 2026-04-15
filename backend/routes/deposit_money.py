from fastapi import APIRouter
from models.db_manager import get_current_users, import_data_to_db
from models.hashing import verify

app = APIRouter(
    tags=["Money Management"]
)

@app.put("/deposit-money/{account_pin}/{money_to_deposit}")
def deposit_money(account_pin: str, money_to_deposit: float) -> dict:
    try:
        users: dict = get_current_users("database/users.json")
        for user, user_data in users.items():
            if verify(user_data["account_pin"], account_pin):
                user_data["balance"] += money_to_deposit

                import_data_to_db("database/users.json", users)
                del user_data["account_pin"]
                
                return {
                    "message": "money sucessfully deposited",
                    "deposited_money": money_to_deposit,
                    "account_details": {
                            user: user_data
                        }
                    }
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}