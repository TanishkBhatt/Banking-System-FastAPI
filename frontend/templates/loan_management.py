import streamlit as st
import requests
from .utils import loan_config

def loan_management():
    st.title("LOAN MANAGEMENT")
    st.markdown(f"compound interest | {loan_config['interest_rate']}% interest rate".upper())
    st.divider()

    st.subheader("BORROW LOAN")
    with st.form(key='borrow-loan'):
        account_pin = st.text_input("ENTER YOUR ACCOUNT PIN")
        money_to_borrow = st.number_input("ENTER MONEY AMOUNT TO BORROW", min_value=1, value=1000, step=1)
        time_duration = st.number_input("ENTER TIME DURATION FOR THE LOAN (MONTHS)", min_value=3, value=12, step=3)
        borrow = st.form_submit_button("BORROW LOAN", type="primary")
        st.markdown("")

        if borrow:
            if account_pin.strip():
                res = requests.put(f"http://127.0.0.1:8000/borrow-loan/{account_pin}/{money_to_borrow}/{time_duration}")
                data = res.json()
                
                if data:
                    if data["message"] == "loan successfully transfered":
                        money_borrowed = data["money_borrowed"]
                        account_details = data["account_details"]
                        loan_history = data["loan_history"]

                        st.success(data["message"].upper())
                        st.info(f"LOAN BORROWED : $ {money_borrowed}")
                        st.markdown("")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("#### ACCOUNT DETAILS")
                            st.dataframe(account_details)
                        with col2:
                            st.markdown("#### LOAN HISTORY")
                            st.dataframe(loan_history)
                        
                    else:
                        st.error(data["message"].upper())
                else:
                    st.error("FAILED TO RETRIEVE DATA")
            else:
                st.warning("PLEASE ENTER THE ACCOUNT PIN TO DEPOSIT")

    st.markdown("")
    st.subheader("CLEAR LOAN")
    with st.form(key='clear-loan'):
        account_pin = st.text_input("ENTER YOUR ACCOUNT PIN")
        clear = st.form_submit_button("CLEAR LOAN", type="primary")
        st.markdown("")

        if clear:
            if account_pin.strip():
                res = requests.put(f"http://127.0.0.1:8000/clear-loan/{account_pin}")
                data = res.json()
                
                if data:
                    if data["message"] == "loan successfully cleared":
                        money_cleared = data["loan_cleared"]
                        account_details = data["account_details"]
                        loan_history = data["loan_history"]

                        st.success("LOAN SUCCESSFULLY CLEARED")
                        st.info(f"LOAN CLEARED : $ {money_cleared}")
                        st.markdown("")

                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("#### ACCOUNT DETAILS")
                            st.dataframe(account_details)
                        with col2:
                            st.markdown("#### LOAN HISTORY")
                            st.dataframe(loan_history)
                    else:
                        st.error(data["message"].upper())
                else:
                    st.error("FAILED TO RETRIEVE DATA")
            else:
                st.warning("PLEASE ENTER THE ACCOUNT PIN TO TRANSACT")

    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")