from fastapi import APIRouter
from models.db_manager import get_current_users

app = APIRouter(
     tags=["Current Users"]
)

@app.get("/activity-status")
def activity_status() -> dict:
    try :
        df = dict(
            total_users=0,
            total_money=0,
            total_loan_takers=0,
            total_money_loan_given=0
        )

        users: dict = get_current_users("database/users.json")

        for user in users.values():
            df["total_users"] += 1
            df["total_money"] += user["balance"]

            if user["loan"] > 0:
                df["total_loan_takers"] += 1
                df["total_money_loan_given"] += user["loan"]

        return {
            "message": "data successfully retrieved",
            "datasets": df
            }
            
    except Exception as e:
        return {"message": f"something went wrong - {str(e)}"}