import streamlit as st
import requests


def home():
    try:
        res = requests.get("http://127.0.0.1:8000/")
        status = "BACKEND SUCCESFULLY CONNECTED" if res.status_code == 200 else "BACKEND ERROR"
    except:
        status = "BACKEND OFFLINE"

    with st.container():
        st.title("BANKING SYSTEM - FASTAPI")
        st.markdown("WELCOME TO YOUR BANKING CONTROL PANEL")
        st.divider()

    with st.container():
        st.subheader("SYSTEM STATUS")
        st.success(status) if "CONNECTED" in status else st.error(status)

    st.divider()

    st.subheader("FEATURES")
    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("#### ACCOUNT MANAGEMENT")
            st.write("CREATE | UPDATE | DELETE ACCOUNTS")

        with st.container(border=True):
            st.markdown("#### MONEY MANAGEMENT")
            st.write("DEPOSIT | WITHDRAW | TRANSFER MONEY")

    with col2:
        with st.container(border=True):
            st.markdown("#### LOAN MANAGEMENT")
            st.write("BORROW | TRACK | CLEAR LOANS")

        with st.container(border=True):
            st.markdown("#### HISTORY TRACKING")
            st.write("TRANSACTIONS | LOANS HISTORY")

    st.divider()

    st.subheader("ABOUT")
    st.markdown("")

    col1, col2 = st.columns([1, 1])

    with col1:
        with st.container(border=True):
            st.markdown("#### TECH STACK")
            st.markdown("""
            - FASTAPI - BACKEND INTEGRATION
            - STREAMLIT - FRONTEND INTEGRATION
            - JSON - DATABASE STORAGE
            """.title())
            st.markdown("")

    with col2:
        with st.container(border=True):
            st.markdown("#### SYSTEM OVERVIEW")
            st.markdown("""
            THIS FULL STACK APPLICATION IS DESIGNED TO SIMULATE REAL-WORLD BANKING WORK FLOWS AND EXPLORE CHALLANGES.  
            """.title())

    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")