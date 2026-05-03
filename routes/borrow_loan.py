from fastapi import APIRouter
from utils.db_manager import access_users, import_data_to_db
from utils.hashing import verify, hash_pin

app = APIRouter(
    tags=["Loan Management"]
)

@app.put("/borrow-loan/{account_pin}/{money_to_borrow}/{time_duration}")
def borrow_loan(account_pin: str, money_to_borrow: float, time_duration: int) -> dict:
    try:
        users: dict = access_users("database/accounts.json")
        users_history: dict = access_users("database/user_history.json")
        loan_config: dict = access_users("database/loan_config.json")

        for pin, user_data in users.items():
            if verify(pin, account_pin):
                if user_data["loan"] == 0:
                    if money_to_borrow <= loan_config["person_loan_limit"]:
                        if money_to_borrow <= loan_config["global_loan_limit"]:
                            if time_duration <= loan_config["max_duration"]:
                                user_data["loan"] = money_to_borrow
                                user_data["balance"] += money_to_borrow
                                loan_config["global_loan_limit"] -= money_to_borrow

                                for pin, history in users_history.items():
                                    if verify(pin, account_pin):
                                        history["loan_history"].append(
                                            {
                                                "loan_status": "pending",
                                                "money": money_to_borrow,
                                                "duration": time_duration,
                                                "rate_of_interest": loan_config["interest_rate"]
                                            }
                                        )
                                        import_data_to_db("database/accounts.json", users)
                                        import_data_to_db("database/user_history.json", users_history)
                                        import_data_to_db("database/loan_config.json", loan_config)

                                        return {
                                            "message": "loan successfully transfered",
                                            "money_borrowed": money_to_borrow,
                                            "account_details": user_data,
                                            "loan_history": history["loan_history"]
                                        }

                                return {"message": "error - user history not found"}
                            return {"message": f"you can't borrow the loan for such a long period. maximum limit : {loan_config["person_loan_limit"]}"}
                        return {"message": f"sorry but our loan system didn't have much money. money limit : {loan_config["global_loan_limit"]}"}
                    return {"message": f"you can't borrow such a large amount. maximim limit : {loan_config["time_duration"]}"}
                return {"message": "you already had an loan uncleared, first clear that"}
            
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}