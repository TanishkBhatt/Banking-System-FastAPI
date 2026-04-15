import streamlit as st
import requests

def current_users():
    st.title("CURRENT USERS")
    st.divider()

    res = requests.get("http://127.0.0.1:8000/activity-status")
    data = res.json()

    if data:
        if data["message"] == "data successfully retrieved":
            datasets = data["datasets"]

            col1, col2 = st.columns(2)
            with col1:
                st.metric("TOATL USERS REGISTERED", 
                            value=f"{datasets["total_users"]} USERS", 
                            delta="+ 5 USERS")
                st.metric("TOTAL LOAN TAKERS",
                          value=f"{datasets["total_loan_takers"]} USERS",
                          delta="+ 2 USERS")

            with col2:
                st.metric("TOATL MONEY DEPOSITED", 
                            value=f"$ {datasets["total_money"]}", 
                            delta="+ $5000000")
                
                st.metric("TOTAL LOAN BORROWD BY USERS",
                          value=f"${datasets["total_money_loan_given"]}",
                          delta="+ $10000")
        else:
            st.error(data["message"].upper())
    else:
        st.error('FAILED TO RETRIEVE DATA')

    st.divider()

    res = requests.get("http://127.0.0.1:8000/get-all-users/")
    data = res.json()

    if data["message"] == "data sucessfully recieved":
        df = data["user_data"]
        st.subheader("ALL USERS DETAILS")
        st.markdown("")
        st.dataframe(df)
        st.divider()
    else:
        st.error(data["message"].upper())

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