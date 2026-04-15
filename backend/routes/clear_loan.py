from fastapi import APIRouter
from models.db_manager import get_current_users, import_data_to_db
from models.hashing import verify
from models.interest_calc import compound_interest

app = APIRouter(
    tags=["Loan Management"]
)

# LOAN CONFIG
LOAN_LIMIT = 10000000
INTEREST_RATE = 18

@app.put("/clear-loan/{account_pin}")
def clear_loan(account_pin: str) -> dict:
    try:
        users: dict = get_current_users("database/users.json")

        for username, user_data in users.items():
            if verify(user_data["account_pin"], account_pin):
                if user_data["loan"]:
                    if user_data["loan"] < user_data["balance"]:
                        amount = compound_interest(user_data["loan"], INTEREST_RATE, 1)
                        user_data["loan"] = 0
                        user_data["balance"] -= amount

                        import_data_to_db("database/users.json", users)
                        del user_data["account_pin"]

                        return {
                            "message": "loan successfully cleared from your account",
                            "loan_cleared": f"${amount} transacted including intrest",
                            "account_details": user_data
                        }
                    return {"message": "you don't have much balance to clear the loan"}
                return {"message": "you don't have any loan to clear"}
                
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}