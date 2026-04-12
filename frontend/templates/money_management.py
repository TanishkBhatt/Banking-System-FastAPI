import streamlit as st
import requests

def money_management():
    st.title("MONEY MANAGEMENT")
    st.divider()

    st.subheader("DEPOSIT MONEY")
    with st.form(key='deposit-money'):
        account_pin = st.text_input("ENTER YOUR ACCOUNT PIN")
        money = st.number_input("ENTER MONEY AMOUNT TO DEPOSIT", min_value=1, value=1000, step=1)
        deposit = st.form_submit_button("DEPOSIT MONEY", type="primary")
        st.markdown("")

        if deposit:
            if account_pin.strip():
                res = requests.put(f"http://127.0.0.1:8000/deposit-money/{account_pin}/{money}")
                data = res.json()
                
                if data["message"] == "money sucessfully deposited":
                    money_deposited = data["deposited_money"]
                    account_details = data["account_details"]

                    st.success("MONEY SUCCESSFULLY DEPOSITED")
                    st.info(f"MONEY DEPOSITED : {money_deposited}")
                    st.markdown("")
                    st.markdown("#### ACCOUNT DETAILS")
                    st.dataframe(account_details)
                else:
                    st.error(data["message"].upper())
            else:
                st.warning("PLEASE ENTER THE ACCOUNT PIN TO DEPOSIT")

    st.markdown("")
    st.subheader("TRANSACT MONEY")
    with st.form(key='tracsact-money'):
        account_pin = st.text_input("ENTER YOUR ACCOUNT PIN")
        money = st.number_input("ENTER MONEY AMOUNT TO DEPOSIT", min_value=1, value=1000, step=1)
        transact = st.form_submit_button("TRANSACT MONEY", type="primary")
        st.markdown("")

        if transact:
            if account_pin.strip():
                res = requests.put(f"http://127.0.0.1:8000/transact-money/{account_pin}/{money}")
                data = res.json()
                
                if data["message"] == "money sucessfully transacted":
                    money_transacted = data["transacted_money"]
                    account_details = data["account_details"]

                    st.success("MONEY SUCCESSFULLY TRANSACTED")
                    st.info(f"MONEY TRANSACTED : {money_transacted}")
                    st.markdown("")
                    st.markdown("#### ACCOUNT DETAILS")
                    st.dataframe(account_details)
                else:
                    st.error(data["message"].upper())
            else:
                st.warning("PLEASE ENTER THE ACCOUNT PIN TO TRANSACT")

    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")