from fastapi import APIRouter
from models.db_manager import get_current_users, import_data_to_db
from models.hashing import verify

app = APIRouter(
    tags=["Money Management"]
)

@app.put("/transfer-money/{your_pin}/{recievers_pin}/{money_to_transfer}")
def transfer_money(your_pin: str, recievers_pin: str, money_to_transfer: float) -> dict:
    try:
        return {}
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}