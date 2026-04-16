import streamlit as st
import requests

def kpi_metrics():
    res = requests.get("http://127.0.0.1:8000/activity-status")
    data = res.json()

    if data:
        if data["message"] == "data successfully retrieved":
            datasets = data["datasets"]

            col1, col2 = st.columns(2)
            with col1:
                st.metric("TOATL USERS REGISTERED", 
                            value=f"{datasets["total_users"]} USERS", 
                            delta=f"+ {datasets["total_users"] // 2} USERS")
                st.metric("TOTAL LOAN TAKERS",
                          value=f"{datasets["total_loan_takers"]} USERS",
                          delta=f"+ {datasets["total_loan_takers"] // 3} USERS")

            with col2:
                st.metric("TOATL MONEY DEPOSITED", 
                            value=f"$ {datasets["total_money"]}", 
                            delta=f"+ ${datasets["total_money"] // 2}")
                
                st.metric("TOTAL LOAN BORROWD BY USERS",
                          value=f"${datasets["total_money_loan_given"]}",
                          delta=f"+ ${datasets["total_money_loan_given"] // 3}")
        else:
            st.error(data["message"].upper())
    else:
        st.error('FAILED TO RETRIEVE DATA')