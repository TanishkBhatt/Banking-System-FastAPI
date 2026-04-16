import streamlit as st
import requests
from .kpi_metrics import kpi_metrics
from streamlit_option_menu import option_menu

def home():
    st.title("BANKING SYSTEM - FASTAPI")
    st.divider()

    # Connection Insurance
    requests.get("http://127.0.0.1:8000/")

    st.subheader("INTRODUCTION")
    st.markdown("a simple **banking system** built using python to simulate real world system workflows. handing user accounts, money management and loan management.".title())

    st.divider()

    kpi_metrics()

    st.divider()

    st.subheader("FEATURES")
    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("ACCOUNT MANAGEMENT"):
            st.markdown("""
            - Create and manage user accounts
            - Store user details like name, email and balance
            - Secure account identification using unique PINs
            """.title())

        with st.expander("VALIDATION AND AUTHENTICATION"):
            st.markdown("""
            - Input validation for all user data
            - Secure authentication using account PIN
            - Prevention of invalid or unauthorized access
            """.title())

        with st.expander("DEPOSITION AND TRANSACTION"):
            st.markdown("""
            - Deposit money into user accounts
            - Withdraw funds securely
            - Real-time balance updates after each transaction
            """.title())

        with st.expander("MONEY TRANSFERRING"):
            st.markdown("""
            - Transfer money between accounts
            - Validation of sender and receiver accounts
            - Safe and consistent transaction handling
            """.title())

    with col2:
        with st.expander("CURRENT USERS DETAILS"):
            st.markdown("""
            - View all registered users
            - Display account details and balances
            - Organized and readable data format
            """.title())

        with st.expander("KPI METRICS"):
            st.markdown("""
            - Total users in the system
            - Total bank balance overview
            - Insights into system activity and growth
            """.title())

        with st.expander("LOAN MANAGEMENT SYSTEM"):
            st.markdown("""
            - Apply for loans
            - Track loan status and repayments
            - Manage user liabilities efficiently
            """.title())

        with st.expander("OPEN SOURCE PROJECT"):
            st.markdown("""
            - Fully open-source and customizable
            - Built using FastAPI and Streamlit
            - Easy to extend with new features
            """.title())

    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("")
        st.button("__NAVIGATE AND EXPLORE__", type="primary")
    
    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")