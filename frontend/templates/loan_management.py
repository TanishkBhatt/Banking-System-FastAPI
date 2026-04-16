import streamlit as st
import requests

def loan_management():
    st.title("LOAN MANAGEMENT")
    st.markdown("compound interest loan at a rate of 18% for 1 year".upper())
    st.divider()

    st.subheader("BORROW LOAN")
    with st.form(key='deposit-money'):
        account_pin = st.text_input("ENTER YOUR ACCOUNT PIN")
        money_to_borrow = st.number_input("ENTER MONEY AMOUNT TO DEPOSIT", min_value=1, value=1000, step=1)
        borrow = st.form_submit_button("BORROW LOAN", type="primary")
        st.markdown("")

        if borrow:
            if account_pin.strip():
                res = requests.put(f"http://127.0.0.1:8000/borrow-loan/{account_pin}/{money_to_borrow}")
                data = res.json()
                
                if data:
                    if data["message"] == "loan successfully transfered to your account":
                        money_borrowed = data["money_borrowed"]
                        account_details = data["account_details"]

                        st.success("LOAN SUCCESSFULLY BORROWED")
                        st.info(f"LOAN BORROWED : {money_borrowed}")
                        st.markdown("")
                        st.markdown("#### ACCOUNT DETAILS")
                        st.dataframe(account_details)
                    else:
                        st.error(data["message"].upper())
                else:
                    st.error("FAILED TO RETRIEVE DATA")
            else:
                st.warning("PLEASE ENTER THE ACCOUNT PIN TO DEPOSIT")

    st.markdown("")
    st.subheader("CLEAR LOAN")
    with st.form(key='tracsact-money'):
        account_pin = st.text_input("ENTER YOUR ACCOUNT PIN")
        clear = st.form_submit_button("CLEAR LOAN", type="primary")
        st.markdown("")

        if clear:
            if account_pin.strip():
                res = requests.put(f"http://127.0.0.1:8000/clear-loan/{account_pin}")
                data = res.json()
                
                if data:
                    if data["message"] == "loan successfully cleared from your account":
                        money_cleared = data["loan_cleared"]
                        account_details = data["account_details"]

                        st.success("LOAN SUCCESSFULLY CLEARED")
                        st.info(f"LOAN CLEARED : {money_cleared.upper()}")
                        st.markdown("")
                        st.markdown("#### ACCOUNT DETAILS")
                        st.dataframe(account_details)
                    else:
                        st.error(data["message"].upper())
                else:
                    st.error("FAILED TO RETRIVE DATA")
            else:
                st.warning("PLEASE ENTER THE ACCOUNT PIN TO TRANSACT")

    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")