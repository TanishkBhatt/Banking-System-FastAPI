from fastapi import APIRouter
from utils.db_manager import access_users, import_data_to_db
from utils.hashing import hash_pin
from datetime import datetime

app = APIRouter(
    tags=["Money Management"]
)

@app.put("/transfer-money/{senders_pin}/{recievers_pin}/{money_to_transfer}")
def transfer_money(senders_pin: str, recievers_pin: str, money_to_transfer: float) -> dict:
    try:
        user_accounts: dict = access_users("database/accounts.json")
        users_history: dict = access_users("database/user_history.json")

        try:
            sender_account = user_accounts[hash_pin(senders_pin)]
            reciever_account = user_accounts[hash_pin(recievers_pin)]
        except KeyError:
            return {"message": "invalid account pins"}
        else:
            try:
                sender_history = users_history[hash_pin(senders_pin)]
                reciever_history = users_history[hash_pin(recievers_pin)]
            except KeyError:
                return {"message": "users history not found, money not transfered"}
            else:
                if sender_account["balance"] > money_to_transfer:
                    user_accounts[hash_pin(senders_pin)]["balance"] -= money_to_transfer
                    user_accounts[hash_pin(recievers_pin)]["balance"] += money_to_transfer

                    users_history[hash_pin(senders_pin)]["transaction_history"].append(
                            {
                                "status": "transferred",
                                "money": money_to_transfer,
                                "to": reciever_account["name"],
                                "datetime": str(datetime.today().strftime("%d/%m/%Y, %H:%M:%S"))
                            }
                        )
                    users_history[hash_pin(recievers_pin)]["transaction_history"].append(
                            {
                                "status": "recieved",
                                "money": money_to_transfer,
                                "from": sender_account["name"],
                                "datetime": str(datetime.today().strftime("%d/%m/%Y, %H:%M:%S"))
                            }
                        )

                    import_data_to_db("database/accounts.json", user_accounts)
                    import_data_to_db("database/user_history.json", users_history)

                    return {
                        "message": "money successfully transfered",
                        "money": money_to_transfer,
                        "from": sender_account["name"],
                        "to": reciever_account["name"],
                        "sender_details": user_accounts[hash_pin(senders_pin)],
                        "sender_history": users_history[hash_pin(senders_pin)]["transaction_history"],
                        "reciever_details": user_accounts[hash_pin(recievers_pin)],
                        "reciever_history": users_history[hash_pin(recievers_pin)]["transaction_history"]
                        }

                return {"message": "the sender does not have much money to transfer"}
    
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}