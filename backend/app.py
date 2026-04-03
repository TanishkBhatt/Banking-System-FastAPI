from fastapi import FastAPI
from models.schema import User, EmailModel, USER_ACCOUNT_KEYS
from models.utils import get_current_users, import_data_to_db
from pydantic import EmailStr
import json

app = FastAPI()

@app.get("/")
def home() -> dict:
    return {"message": "welcome to banking management system"}

@app.get("/get-all-users")
def get_all_users() -> dict:
    data = get_current_users("database/users.json")
    return data

@app.get("/get-user-by-pin")
def get_user_by_pin(account_pin: int) -> dict:
    users = get_current_users("database/users.json")
    for key, user in users.items():
        if user["account_pin"] == account_pin:
            data = users[key]
            return data
    return {"message": "invalid account pin"}

@app.post("/create-new-account")
def create_new_account(name: str, age: int, address: str, email: EmailStr, account_pin: int, balance: float) -> dict:
    users = get_current_users("database/users.json")
    invalid_pins = []

    if users:
        next_user = str(int(list(users.keys())[-1]) + 1)
        for user in users.values():
            invalid_pins.append(user["account_pin"])
    else:
        next_user = "1"

    if account_pin not in invalid_pins:
        user_data = User(**{
            "name": name,
            "age": age,
            "address": address,
            "email": email,
            "account_pin": account_pin,
            "balance": balance
        })
        users[next_user] = user_data.model_dump()
        import_data_to_db("database/users.json", users)
        return {"message": "account sucessfully created"}

    return {"message": "this account pin has been already taken"}

@app.put("/update-account")
def update_account(account_pin: int, updating_key: str, updated_value: str) -> dict:
    if updating_key not in USER_ACCOUNT_KEYS:
        return {"message": "invalid key to update"}
    
    users = get_current_users("database/users.json")
    for key, user in users.items():
        if users[key]["account_pin"] == account_pin:
            match updating_key:
                case "name":
                    users[key][updating_key] = updated_value
                case "address":
                    users[key][updating_key] = updated_value
                case "age": 
                    users[key][updating_key] = int(updated_value)
                case "account_pin": 
                    users[key][updating_key] = int(updated_value)
                case "email": 
                    EmailModel(email=updated_value)
                    users[key][updating_key] = updated_value
                case "balance":
                    users[key][updating_key] = float(updated_value)
                case _ : 
                    pass

            import_data_to_db("database/users.json", users)
            return {"message": "details sucessfully updated"}

@app.delete("/delete-account")
def delete_account(account_pin: int) -> dict:
    users = get_current_users("database/users.json")

    for key, user in users.items():
        if user["account_pin"] == account_pin:
            del users[key]

            import_data_to_db("database/users.json", users)
            return {"message": "account sucessfully deleted"}

    return {"message": "invalid account pin"}
