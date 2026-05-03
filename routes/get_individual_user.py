from fastapi import APIRouter
from utils.db_manager import access_users
from utils.hashing import verify

app = APIRouter(
     tags=["Current Users"]
)

@app.get("/get-indvidual-user/{account_pin}")
def get_indvidual_user(account_pin: str) -> dict:
    try:
        user_accounts: dict = access_users("database/accounts.json")
        users_history: dict = access_users("database/user_history.json")
        
        for pin, data in user_accounts.items():
            if verify(pin, account_pin):
                user_details = data

                for pin, history in users_history.items():
                    if verify(pin, account_pin):
                        user_history = history
    
                        return {
                            "message": "data sucessfully recieved",
                            "user_details": user_details,
                            "user_history": user_history
                            }

                return {'message': "user history not found"}
        return {"message": "this account pin does not exists"}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}