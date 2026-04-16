import streamlit as st
import requests
from .kpi_metrics import kpi_metrics

def current_users():
    st.title("CURRENT USERS")
    st.divider()

    kpi_metrics()

    st.divider()

    res = requests.get("http://127.0.0.1:8000/get-all-users/")
    data = res.json()

    if data:
        if data["message"] == "data sucessfully recieved":
            df = data["user_data"]
            st.subheader("ALL USERS DETAILS")
            st.markdown("")
            st.dataframe(df)
            st.divider()
        else:
            st.error(data["message"].upper())
    else:
        st.error("FAILED TO RETRIVE DATA")

    st.subheader("GET INDIVIDUAL USER")
    st.markdown("")
    
    with st.form(key='get_ind_user'):
        account_pin = st.text_input("ENTER THE ACCOUNT PIN TO FETCH DATA OF")
        get_data = st.form_submit_button("RETRIEVE ACCOUNT DATA", type="primary")

    if get_data:
        if account_pin.strip():
            res = requests.get(f"http://127.0.0.1:8000//get-indvidual-user/{account_pin}")
            data = res.json()
            if data:
                if data["message"] == "data sucessfully recieved":
                    df = data["user_data"]
                    st.markdown("#### RECIEVED DATA")
                    st.dataframe(df)
                else:
                    st.error(data["message"].upper())
            else:
                st.error("FAILED TO RETRIVE DATA")
        else:
            st.warning("PLEASE ENTER THE ACCOUNT PIN")
            
    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")