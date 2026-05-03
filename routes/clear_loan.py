from fastapi import APIRouter
from utils.db_manager import access_users, import_data_to_db
from utils.hashing import verify
from utils.interest import compound_interest

app = APIRouter(
    tags=["Loan Management"]
)

@app.put("/clear-loan/{account_pin}")
def clear_loan(account_pin: str) -> dict:
    try:
        users: dict = access_users("database/accounts.json")
        users_history: dict = access_users("database/user_history.json")
        loan_config: dict = access_users("database/loan_config.json")

        for pin, user_data in users.items():
            if verify(pin, account_pin):
                if user_data["loan"]:
                    for pin, history in users_history.items():
                        if verify(pin, account_pin):
                            amount = compound_interest(
                                history["loan_history"][-1]["money"], 
                                history["loan_history"][-1]["rate_of_interest"], 
                                history["loan_history"][-1]["duration"]/12
                            )
                            if amount < user_data["balance"]:
                                user_data["loan"] = 0.0
                                user_data["balance"] -= amount
                                loan_config["global_loan_limit"] += amount

                                history["loan_history"][-1]["loan_status"] = "cleared"
                                history["loan_history"][-1]["money_transacted"] = amount

                                import_data_to_db("database/accounts.json", users)
                                import_data_to_db("database/user_history.json", users_history)
                                import_data_to_db("database/loan_config.json", loan_config)

                                return {
                                    "message": "loan successfully cleared",
                                    "loan_cleared": amount,
                                    "account_details": user_data,
                                    "loan_history": history["loan_history"]
                                }
                            return {"message": f"you don't have much balance to clear. loan amount : {amount}"}

                    return {"message": "error - user history not found"}
                return {"message": "you don't have any loan to clear"}
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}