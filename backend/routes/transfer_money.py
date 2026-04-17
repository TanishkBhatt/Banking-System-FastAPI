from fastapi import APIRouter
from utils.db_manager import get_current_users, import_data_to_db
from utils.hashing import verify

app = APIRouter(
    tags=["Money Management"]
)

@app.put("/transfer-money/{senders_pin}/{recievers_pin}/{money_to_transfer}")
def transfer_money(senders_pin: str, recievers_pin: str, money_to_transfer: float) -> dict:
    try:
        users: dict = get_current_users("database/users.json")

        is_sender = False
        is_reciever = False

        for username, user_data in users.items():
            if verify(user_data["account_pin"], senders_pin):
                sender = {"username": username,
                          "data": user_data}
                is_sender = True

            if verify(user_data["account_pin"], recievers_pin):
                reciever = {"username": username,
                          "data": user_data}
                is_reciever = True

        if is_sender and is_reciever:
            if sender["data"]["balance"] >= money_to_transfer:
                users[sender["username"]]["balance"] -= money_to_transfer
                users[reciever["username"]]["balance"] += money_to_transfer

                import_data_to_db("database/users.json", users)

                del sender["data"]["account_pin"]
                del reciever["data"]["account_pin"]

                return {
                    "message": "money successfully transfered",
                    "money_transfered": money_to_transfer,
                    "from": sender["data"]["name"],
                    "to": reciever["data"]["name"],
                    "sender_details": sender["data"],
                    "reciever_details": reciever["data"]
                    }
            
            return {"message": "the sender does not have much money to transfer"}
        return {"message": "these account pins does not exists"}
    
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}