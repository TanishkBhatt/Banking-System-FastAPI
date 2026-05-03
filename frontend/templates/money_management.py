import streamlit as st
import requests

def money_management():
    st.title("MONEY MANAGEMENT")
    st.markdown("DEPOSIT | WITHDRAW | TRANSFER MONEY")
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
                
                if data:
                    if data["message"] == "money sucessfully deposited":
                        money_deposited = data["deposited_money"]

                        st.success("MONEY SUCCESSFULLY DEPOSITED")
                        st.info(f"MONEY DEPOSITED : $ {money_deposited}")
                        st.markdown("")

                        user_details = data["account_details"]
                        user_history = data["account_history"]

                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("#### ACCOUNT DETAILS")
                            st.dataframe(user_details)
                        with col2:
                            st.markdown("#### LATEST DEPOSITS")
                            st.dataframe(user_history)
                    else:
                        st.error(data["message"].upper())
                else:
                    st.error("FAILED TO RETRIEVE DATA")
            else:
                st.warning("PLEASE ENTER THE ACCOUNT PIN TO DEPOSIT")

    st.markdown("")
    st.subheader("WITHDRAW MONEY")
    with st.form(key='withdraw-money'):
        account_pin = st.text_input("ENTER YOUR ACCOUNT PIN")
        money = st.number_input("ENTER MONEY AMOUNT TO WITHDRAW", min_value=1, value=1000, step=1)
        transact = st.form_submit_button("WITHDRAW MONEY", type="primary")
        st.markdown("")

        if transact:
            if account_pin.strip():
                res = requests.put(f"http://127.0.0.1:8000/withdraw-money/{account_pin}/{money}")
                data = res.json()
                
                if data:
                    if data["message"] == "money sucessfully withdrawal":
                        money_withdrawal = data["withdrawal_money"]

                        st.success("MONEY SUCCESSFULLY TRANSACTED")
                        st.info(f"MONEY WITHDRAWAL : $ {money_withdrawal}")
                        st.markdown("")
                        
                        user_details = data["account_details"]
                        user_history = data["account_history"]

                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("#### ACCOUNT DETAILS")
                            st.dataframe(user_details)
                        with col2:
                            st.markdown("#### LATEST TRANSACTIONS")
                            st.dataframe(user_history)
                    else:
                        st.error(data["message"].upper())
                else:
                    st.error("FAILED TO RETRIVE DATA")
            else:
                st.warning("PLEASE ENTER THE ACCOUNT PIN TO TRANSACT")

    st.markdown("")
    st.subheader("TRANSFER MONEY")
    
    with st.form(key='transfer-money'):
        sender_pin = st.text_input("ENTER SENDER'S ACCOUNT PIN")
        reciever_pin = st.text_input("ENTER RECIEVER'S ACCOUNT PIN")
        money = st.number_input("ENTER MONEY AMOUNT TO TRANSFER", min_value=1, value=1000, step=1)
        transfer = st.form_submit_button("TRANSFER MONEY", type="primary")
        st.markdown("")

        if transfer:
            if sender_pin.strip() and reciever_pin.strip():
                if sender_pin.strip() != reciever_pin.strip():
                    res = requests.put(f"http://127.0.0.1:8000/transfer-money/{sender_pin}/{reciever_pin}/{money}")
                    data = res.json()
                    
                    if data:
                        pass
                        if data["message"] == "money successfully transfered":
                            from_ = data["from"]
                            to_ = data["to"]
                            money_transfered = data["money"]
                            sender_details = data["sender_details"]
                            sender_history = data["sender_history"]
                            reciever_details = data["reciever_details"]
                            reciever_history = data["reciever_history"]

                            st.success("MONEY SUCCESSFULLY TRANSFERED")
                            st.info(f"MONEY TRANSFERED : $ {money_transfered}")

                            col1, col2 = st.columns(2)
                            with col1:
                                st.info(f"FROM : {from_}")
                            with col2:
                                st.info(f"TO : {to_}")

                            st.markdown("")
                            st.markdown("#### ACCOUNT DETAILS")

                            col1, col2 = st.columns(2)
                            with col1:
                                st.dataframe(sender_details)
                                st.dataframe(sender_history)
                            with col2:
                                st.dataframe(reciever_details)
                                st.dataframe(reciever_history)

                        else:
                            st.error(data["message"].upper())
                    else:
                        st.error("FAILED TO RETRIVE DATA")
                else:
                    st.error("SENDER'S PIN AND RECIEVER'S PIN CAN'T BE SAME")
            else:
                st.warning("PLEASE ENTER THE ACCOUNT PINS TO TRANSFER MONEY")

    st.divider()
    st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")