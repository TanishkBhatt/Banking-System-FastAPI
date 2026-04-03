from fastapi import APIRouter
from pydantic import ValidationError
from models.schema import EmailModel, UPDATEABLE_KEYS
from models.utils import get_current_users, import_data_to_db

app = APIRouter()

@app.put("/update-account-details")
def update_account_details(account_pin: str, updating_key: str, updated_value: str|int|EmailModel) -> dict:
    if updating_key not in UPDATEABLE_KEYS:
        return {"message": "invalid key to update"}
    
    users = get_current_users("database/users.json")
    for key, _ in users.items():
        if users[key]["account_pin"] == account_pin:
            match updating_key:
                case "email": 
                    try:
                        validate_email = EmailModel(email=updated_value)
                        users[key][updating_key] = validate_email.email
                    except ValidationError:
                        return {"message": "invalid email formal to update"}
                case "age":
                    users[key][updating_key] = int(updated_value)
                case _ :
                    users[key][updating_key] = updated_value

            import_data_to_db("database/users.json", users)
            return {
                "message": "details sucessfully updated",
                "updated_account_details": users[key]
            }