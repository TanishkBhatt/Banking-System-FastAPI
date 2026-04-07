import json

def get_current_users(filepath: str) -> dict:
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

def import_data_to_db(filepath: str, data: dict) -> None:
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

# from pymongo import MongoClient
# from .env import DB_CONNECTION_URL

# def get_current_users() -> list[dict]:
#     client = MongoClient(DB_CONNECTION_URL)
#     database = client["users"]
#     collection = database["user_details"]
#     collection_data = list(collection.find())
#     return collection_data

# def import_data_to_db(data: dict) -> None:
#     client = MongoClient(DB_CONNECTION_URL)
#     db = client["users"]
#     collection = db["user_details"]

#     collection.insert_one(data)