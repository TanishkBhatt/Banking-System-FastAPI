from pydantic import BaseModel, EmailStr
from typing import Literal

class User(BaseModel):
    username: str
    name: str
    age: int
    gender: Literal["MALE", "FEMALE"]
    address: str
    email: EmailStr
    account_pin: str
    balance: float