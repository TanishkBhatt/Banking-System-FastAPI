import streamlit as st
from streamlit_option_menu import option_menu
from templates import *

st.set_page_config("Banking System - FastAPI")
with st.sidebar:
    page = option_menu(
            menu_title="NAVIGATE",
            options=[
                    "HOME",
                    "CURRENT USERS",
                    "ACCOUNT MANAGEMENT",
                    "MONEY MANAGEMENT"
            ])

match page:
    case "HOME":
        home()
    case "CURRENT USERS":
        current_users()
    case "ACCOUNT MANAGEMENT":
        account_management()
    case "MONEY MANAGEMENT":
        money_management()