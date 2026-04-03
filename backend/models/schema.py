from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    age: int
    address: str
    email: EmailStr
    account_pin: int
    balance: float

class EmailModel(BaseModel):
    email: EmailStr

USER_ACCOUNT_KEYS = ["name", "age", "address", "email", "account_pin", "balance"]