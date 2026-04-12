import streamlit as st
import requests

def home():
    st.title("BANKING SYSTEM - FASTAPI")
    st.divider()

    conn = requests.get("http://127.0.0.1:8000/")

    st.subheader("INTRODUCTION")
    st.markdown("a **python** based **banking system** is a real world application handling **account and money management** using **fastapi** as backend engine and **streamlit** as a frontend framework.".title())
    st.markdown("Made By Tanishk - A Student And A Programmer")

    st.divider()
    st.subheader("FEATURES")
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("Real World Application"):
            st.markdown(
                f"""
                - Simulates Real Banking Operations
                - Designed similar to actual Banking Systems
                """
            )
        with st.expander("User Validation"):
            st.markdown(
                f"""
                - Strong Data Validation using Pydantic
                - Prevents invalid data from entering the system
                """
            )
        with st.expander("Account Management"):
            st.markdown(
                f"""
                - Basic CRUD Operations
                - Unique account Identification
                """
            )
    with col2:
        with st.expander("Money Management"):
            st.markdown(
                f"""
                - Supports deposit and transaction of money
                - Ensures safegaurd for insuffcient balance handling
                """
            )
        with st.expander("Activity Status"):
            st.markdown(
                f"""
                - Track Users Activities
                - Provides Insights and Repots
                """
            )
        with st.expander("Technical Stack Used"):
            st.markdown(
                f"""
                - FastAPI - Backend
                - Streamlit - Frontend
                - DataBase - JSON
                """
            )

    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("")
        st.button("__NAVIGATE AND EXPLORE__", type="primary")
    
    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")