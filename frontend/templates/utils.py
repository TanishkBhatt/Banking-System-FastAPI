from pydantic import BaseModel, EmailStr, Field
from typing import Literal
from datetime import date

class User(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    name: str = Field(min_length=3, max_length=30)
    dob: date
    gender: Literal["MALE", "FEMALE"]
    address: str = Field(min_length=3, max_length=100)
    email: EmailStr
    phone: str = Field(pattern=r"^\d{10}$")
    account_pin: str = Field(min_length=6, max_length=10)

loan_config = {
    "person_loan_limit": 10000000,
    "interest_rate": 18,
    "loan_type": "COMPOUND INTREST",
    "max_duration": 48
}