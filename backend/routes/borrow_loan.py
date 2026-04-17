from fastapi import APIRouter
from utils.db_manager import get_current_users, import_data_to_db
from utils.hashing import verify

app = APIRouter(
    tags=["Loan Management"]
)

# LOAN CONFIG
LOAN_LIMIT = 10000000
INTEREST_RATE = 18

@app.put("/borrow-loan/{account_pin}/{money_to_borrow}")
def borrow_loan(account_pin: str, money_to_borrow: float) -> dict:
    try:
        users: dict = get_current_users("database/users.json")
 
        for username, user_data in users.items():
            if verify(user_data["account_pin"], account_pin):
                if user_data["loan"] == 0:
                    if money_to_borrow <= LOAN_LIMIT:
                        user_data["loan"] = money_to_borrow
                        user_data["balance"] += money_to_borrow

                        import_data_to_db("database/users.json", users)

                        del user_data["account_pin"]
                        return {
                            "message": "loan successfully transfered to your account",
                            "money_borrowed": money_to_borrow,
                            "account_details": user_data
                        }
                    return {"message": f"you can't borrow such a large amount. maximim limit : {LOAN_LIMIT}"}
                return {"message": "you already had an loan uncleared, first clear that"}
            
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}