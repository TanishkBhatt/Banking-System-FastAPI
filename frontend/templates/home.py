import streamlit as st
import requests

def home():
    st.title("BANKING SYSTEM - FASTAPI")
    st.divider()

    conn = requests.get("http://127.0.0.1:8000/")

    st.subheader("INTRODUCTION")
    st.markdown("a simple **banking system** built using fastapi as backend and streamlit as frontend, handling user accounts, money management and loan management systems.".title())

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
            st.divider()    
        else:
            st.error(data["message"].upper())
    else:
        st.error('FAILED TO RETRIEVE DATA')

    st.markdown("")
    st.subheader("FEATURES")
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("REAL WORLD USAGE")
        with st.container(border=True):
            st.markdown("ACCOUNT MANAGEMENT")
        with st.container(border=True):
            st.markdown("VALIDATION AND AUTHENTICATION")

    with col2:
        with st.container(border=True):
            st.markdown("MONEY MANAGEMENT")
        with st.container(border=True):
            st.markdown("LOAN MANGEMENET")
        with st.container(border=True):
            st.markdown("OPEN SOURCE PROJECT")

    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("")
        st.button("__NAVIGATE AND EXPLORE__", type="primary")
    
    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")