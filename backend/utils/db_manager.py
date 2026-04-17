import json

def get_current_users(filepath: str) -> dict:
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

def import_data_to_db(filepath: str, data: dict) -> None:
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)