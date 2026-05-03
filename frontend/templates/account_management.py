import streamlit as st
import requests
from pydantic import ValidationError, EmailStr
from typing import Literal
from datetime import date, datetime
from .utils import User

def account_management():
    st.title("ACCOUNT MANAGEMENT")
    st.markdown("CREATE | UPDATE | DELETE ACCOUNTS")
    st.divider()

    st.subheader("CREATE NEW ACCOUNT")
    st.markdown("")

    with st.form(key="create-account"):
        col1, col2 = st.columns(2)
        with col1:
            username: str = st.text_input("ENTER A USERNAME FOR YOUR ACCOUNT")
            name: str = st.text_input("ENTER YOUR FULL NAME")
            dob: date = st.date_input("SELECT YOUR DATE OF BIRTH", 
                                    min_value=datetime(1950, 1, 1),  
                                    max_value=datetime.today(), 
                                    value=datetime(2000, 1,  1))
            gender: Literal["MALE", "FEMALE"] = st.selectbox("SELECT YOUR GENDER", ["MALE", "FEMALE"])

        with col2:
            address: str = st.text_input("ENTER YOUR ADDRESS")
            email: EmailStr = st.text_input("ENTER YOUR EMAIL ADDRESS", value="@gmail.com")
            phone: str = st.text_input("ENTER YOUR PHONE NUMBER")
            account_pin: str = st.text_input("CREATE A SECURE ACCOUNT PIN (6-10 CHARS)", type="password", max_chars=10)

        _, col2, _ = st.columns(3)
        with col2:
            submit = st.form_submit_button("CREATE ACCOUNT", type="primary")

    if submit:
        if username.strip() and name.strip() and address.strip() and email.strip() and account_pin.strip():
            try:
                user_data = User(
                    username=username,
                    name=name,
                    dob=dob,
                    gender=gender,
                    address=address,
                    email=email,
                    phone=phone,
                    account_pin=account_pin,
                )

                res = requests.post(
                                    "http://127.0.0.1:8000/create-account",
                                    json=user_data.model_dump(mode="json"),
                                    headers={"Content-Type": "application/json"}
                                )

                data = res.json()
                if data:
                    if data["message"] == "account successfully created":
                        account_data = data["account_details"]
                        st.success(data["message"].upper())
                        st.markdown("")
                        
                        st.markdown("#### CREATED ACCOUNT DETAILS")
                        st.dataframe(account_data)

                    else:
                        st.error(data["message"].upper())
                else:
                    st.error("FAILED TO RETRIEVE DATA")
            except ValidationError:
                st.error("VALIDATION ERROR : FILL UP THE SUITABLE DATA TYPE")
        else:
            st.warning("PLEASE FILL UP ALL THE DETAILS")

    st.divider()
    st.subheader("UPDATE AN EXISTING ACCOUNT")
    st.markdown("")

    with st.container(border=True):
        account_pin = st.text_input("ENTER YOUR ACCOUNT PIN")
        key_to_update = st.selectbox("SELECT THE KEY TO UPDATE VALUE OF",
                                    ["NAME", "DOB", "GENDER", "ADDRESS", "EMAIL", "PHONE"])
        if key_to_update == "DOB":
            dob: date = st.date_input("SELECT YOUR DATE OF BIRTH TO UPDATE", 
                                        min_value=datetime(1950, 1, 1),  
                                        max_value=datetime.today(), 
                                        value=datetime(2000, 1,  1))
            updated_value = str(dob)
        elif key_to_update == "GENDER":
            updated_value: str = st.selectbox("SELECT YOUR GENDER TO UPDATE", ["MALE", "FEMALE"])
        elif key_to_update == "EMAIL":
            updated_value: str = st.text_input(f"ENTER YOUR {key_to_update} TO UPDATE", value="@gmail.com")
        else:
            updated_value: str = st.text_input(f"ENTER YOUR {key_to_update} TO UPDATE").title()

        update = st.button("UPDATE ACCOUNT", type="primary")
    
    if update:
        if account_pin.strip() and updated_value.strip():
            res = requests.put(f"http://127.0.0.1:8000/update-account/{account_pin}/{key_to_update.lower()}/{updated_value}")
            data = res.json()

            if data:
                if data["message"] == "account successfully updated":
                    st.success(data["message"].upper())
                    st.markdown("")

                    updating_key, updated_value = data["updating_key"], data["updated_value"]
                    account_details = data["account_details"]

                    col1, col2 = st.columns(2)
                    with col1:
                        st.info(f"UPDATING KEY : {updating_key.upper()}")
                    with col2:
                        st.info(f"UPDATED VALUE : {updated_value}")

                    st.markdown("")
                    st.markdown("#### UPDATED ACCOUNT DETAILS")
                    st.dataframe(account_details)
                    
                else:
                    st.error(data["message"].upper())
            else:
                st.error("FAILED TO RETRIVE DATA")
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
                if data["message"] == "account successfully deleted":
                    st.success(data["message"].upper())
                    st.markdown("")

                    deleted_account_details = data["deleted_account_details"]
                    deleted_account_history = data["deleted_account_history"]
                    deleted_account_loan_history = data["deleted_account_loan_history"]

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("#### DELETED ACCOUNT DETAILS")
                        st.dataframe(deleted_account_details)
                        
                    with col2:
                        st.markdown("#### ACCOUNT HISTORY")
                        st.dataframe(deleted_account_history)
                        st.markdown("#### LOAN HISTORY")
                        st.dataframe(deleted_account_loan_history)

                else:
                    st.error(data["message"].upper())
            else:
                st.error("FAILED TO RETRIVE DATA")
        else:
            st.warning("PLEASE ENTER THE ACCOUNT PIN")

    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")