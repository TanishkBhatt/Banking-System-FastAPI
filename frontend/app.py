import streamlit as st
import requests
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

st.set_page_config("Banking System - FastAPI")
st.title("BANKING SYSTEM - FASTAPI")

# ----------- DEMO RESPONSES --------------
res = requests.get("http://127.0.0.1:8000/")                            # Home Route
res = res.json()
st.success(res["message"].upper())

with st.expander("GET ALL USERS DETAILS"):
    users = requests.get("http://127.0.0.1:8000/get-all-users/")        # Get Users Route
    users = users.json()
    st.json(users["data"])

# ----------- TO BE CONTINUED --------------