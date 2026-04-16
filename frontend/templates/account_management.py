import streamlit as st
import requests
from pydantic import BaseModel, EmailStr, ValidationError
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
    loan: float

def account_management():
    st.title("ACCOUNT MANAGEMENT")
    st.divider()

    st.subheader("CREATE NEW ACCOUNT")
    st.markdown("")

    with st.form(key="create-account"):
        col1, col2 = st.columns(2)
        with col1:
            username = st.text_input("ENTER A USERNAME FOR YOUR ACCOUNT")
            name = st.text_input("ENTER YOUR FULL NAME")
            age = st.number_input("ENTER YOUR AGE (IN YEARS)", min_value=18, max_value=100, value=18, step=1)
            gender = st.selectbox("SELECT YOUR GENDER", ["MALE", "FEMALE"])

        with col2:
            address = st.text_input("ENTER YOUR ADDRESS")
            email = st.text_input("ENTER YOUR EMAIL ADDRESS", value="@gmail.com")
            account_pin = st.text_input("CREATE A SECURE PIN FOR YOUR ACCOUNT", type="password", max_chars=10)
            balance = st.number_input("DEPOSIT SOME BALANCE INTO YOUR ACCOUNT", min_value=0.0, value=0.0, step=1.0)

        col1, col2, col3 = st.columns(3)
        with col2:
            submit = st.form_submit_button("CREATE ACCOUNT", type="primary")

    if submit:
        if username.strip() and name.strip() and address.strip() and email.strip() and account_pin.strip():
            try:
                user_data = User(
                    username=username,
                    name=name,
                    age=age,
                    address=address,
                    email=email,
                    account_pin=account_pin,
                    balance=balance,
                    gender=gender,
                    loan=0
                )

                res = requests.post(
                                    "http://127.0.0.1:8000/create-account",
                                    json=user_data.model_dump(mode="json"),
                                    headers={"Content-Type": "application/json"}
                                )

                data = res.json()
                if data:
                    if data["message"] == "account sucessfully created":
                        acc_data = data["account_details"]

                        st.success("ACCOUNT SUCCESSFULLY CREATED")
                        st.markdown("#### CREATED ACCOUNT DATA")
                        st.dataframe(acc_data)

                    else:
                        st.error(data["message"].upper())
                else:
                    st.error("FAILED TO RETRIEVE DATA")

            except ValidationError:
                st.error("PLEASE FILL UP THE SUITABLE DATA TYPE")
        else:
            st.warning("PLEASE FILL UP ALL THE DETAILS")

    st.divider()
    st.subheader("DELETE AN EXISTING ACCOUNT")
    st.markdown("")

    with st.form(key='delete-account'):
        account_pin_to_del = st.text_input("ENTER THE PIN TO DELETE THE ACCOUNT")
        delete = st.form_submit_button("DELETE ACCOUNT", type="primary")

    if delete:
        if account_pin_to_del.strip():
            res = requests.delete(f"http://127.0.0.1:8000/delete-account/{account_pin_to_del}")
            data = res.json()
            if data:
                if data["message"] == "account sucessfully deleted":
                    deleted_account_details = data["deleted_account_details"]
                    
                    st.success("ACCOUNT SUCCESSFULLY DELETED")
                    st.markdown("")

                    st.markdown("#### DELETED ACCOUNT DETAILS")
                    st.dataframe(deleted_account_details)

                else:
                    st.error(data["message"].upper())
            else:
                st.error("FAILED TO RETRIVE DATA")
        else:
            st.warning("PLEASE ENTER THE ACCOUNT PIN")

    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")