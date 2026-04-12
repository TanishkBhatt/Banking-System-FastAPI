from fastapi import APIRouter
from models.db_manager import get_current_users

app = APIRouter()

@app.get("/activity-status")
def activity_status() -> dict:
    try :
        df = dict(
            total_users=0,
            total_money=0,
            age_groups=dict(
                childrens=0,
                teenagers=0,
                adults=0,
                seniors=0
            ),
            gender_groups=dict(
                male=0,
                female=0
            )
        )

        users: dict = get_current_users("database/users.json")

        for user in users.values():
            df["total_users"] += 1
            df["total_money"] += user["balance"]

            age = user["age"]
            if age < 13:
                df["age_groups"]["childrens"] += 1
            elif age < 20:
                df["age_groups"]["teenagers"] += 1
            elif age < 61:
                df["age_groups"]["adults"] += 1
            else:
                df["age_groups"]["seniors"] += 1

            gender = user["gender"]
            if gender == "MALE":
                df["gender_groups"]["male"] += 1
            else:
                df["gender_groups"]["female"] += 1

        return {
            "message": "data successfully retrieved",
            "datasets": df
            }
            
    except Exception as e:
        return {"message": f"something went wrong : {str(e)}"}