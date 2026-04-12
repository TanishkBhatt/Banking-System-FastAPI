import streamlit as st
from pandas import DataFrame
import requests

def current_users():
    st.title("CURRENT USERS")
    st.divider()

    res = requests.get("http://127.0.0.1:8000/get-all-users/")
    data = res.json()
    if data["message"] == "data sucessfully recieved":
        df = DataFrame(data["data"])
        st.subheader("ALL USERS DETAILS")
        st.dataframe(df.T)
        st.divider()
    else:
        st.error(data["message"].upper())

    st.subheader("GET INDIVIDUAL USER")
    account_pin = st.text_input("ENTER THE ACCOUNT PIN TO FETCH DATA OF")
    col1, col2, col3 = st.columns(3)
    with col2:
        get_data = st.button("RETRIEVE ACCOUNT DATA", type="primary")

    if get_data:
        if account_pin.strip():
            res = requests.get(f"http://127.0.0.1:8000//get-indvidual-user/{account_pin}")
            data = res.json()
            if data["message"] == "data sucessfully recieved":
                df = DataFrame(data["data"])
                st.markdown("##### RECIEVED DATA")
                st.dataframe(df)
            else:
                st.error(data["message"].upper())
        else:
            st.warning("FIRST ENTER THE ACCOUNT PIN")
            
    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")