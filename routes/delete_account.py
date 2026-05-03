from fastapi import APIRouter
from utils.db_manager import access_users, import_data_to_db
from utils.hashing import verify, hash_pin

app = APIRouter(
    tags=["Account Management"]
)

@app.delete("/delete-account/{account_pin}")
def delete_account(account_pin: str) -> dict:
    try:
        user_accounts: dict = access_users("database/accounts.json")
        users_history: dict = access_users("database/user_history.json")

        hashed_pin = hash_pin(account_pin)
        
        if hashed_pin in user_accounts.keys() and hashed_pin in users_history.keys():
            if user_accounts[hashed_pin]["loan"] == 0:
                deleted_account_details = user_accounts[hashed_pin]

                if hashed_pin in users_history.keys():
                    deleted_account_history = users_history[hashed_pin]["transaction_history"]
                    deleted_account_loan_history = users_history[hashed_pin]["loan_history"]

                    del user_accounts[hashed_pin]
                    import_data_to_db("database/accounts.json", user_accounts)

                    del users_history[hashed_pin]
                    import_data_to_db("database/user_history.json", users_history)

                    return {
                            "message": "account successfully deleted",
                            "deleted_account_details": deleted_account_details,
                            "deleted_account_history": deleted_account_history,
                            "deleted_account_loan_history": deleted_account_loan_history
                        }

                return {"message": "user history not found, account not deleted."}
            return {"message": "you have a loan pending, first clear that loan."}
        return {"message": "this account pin does not exists in our database."}

    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}