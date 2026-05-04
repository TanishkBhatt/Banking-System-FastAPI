import streamlit as st
import requests

def current_users():
    st.title("CURRENT USERS")
    st.markdown("FETCH ALL CURRENT USERS DATA")
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
        st.error("FAILED TO RETRIEVE DATA")

    st.subheader("GET INDIVIDUAL USER")
    st.markdown("")
    
    with st.form(key='get_individual_user'):
        account_pin = st.text_input("ENTER THE ACCOUNT PIN TO FETCH DATA OF")
        get_data = st.form_submit_button("RETRIEVE ACCOUNT DATA", type="primary")

    if get_data:
        if account_pin.strip():
            res = requests.get(f"http://127.0.0.1:8000/get-indvidual-user/{account_pin}")
            data = res.json()
            if data:
                if data["message"] == "data sucessfully recieved":
                    st.success("DATA SUCCESSFULLY RETRIEVED")
                    st.markdown("")
                    
                    user_details = data["user_details"]
                    user_history = data["user_history"]

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("#### USER DETAILS")
                        st.dataframe(user_details)

                    with col2:
                        st.markdown("#### TRANSACTIONS HISTORY")
                        st.dataframe(user_history["transaction_history"])
                        st.markdown("#### LOAN HISTORY")
                        st.dataframe(user_history["loan_history"])
                else:
                    st.error(data["message"].upper())
            else:
                st.error("FAILED TO RETRIEVE DATA")
        else:
            st.warning("PLEASE ENTER THE ACCOUNT PIN")
            
    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")