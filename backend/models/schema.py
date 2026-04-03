from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    name: str
    age: int
    address: str
    email: EmailStr
    account_pin: str
    balance: float

class EmailModel(BaseModel):
    email: EmailStr

UPDATEABLE_KEYS = ["username", "name", "age", "address", "email"]