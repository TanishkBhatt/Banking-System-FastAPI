from fastapi import FastAPI
from routes import (
    home, 
    get_all_users, 
    get_individual_user, 
    create_account,  
    delete_account,
    deposit_money,
    transact_money,
    activity_status,
    borrow_loan,
    clear_loan,
    transfer_money
)

app = FastAPI()

app.include_router(home.app)
app.include_router(get_all_users.app)
app.include_router(get_individual_user.app)
app.include_router(create_account.app)
app.include_router(delete_account.app)
app.include_router(deposit_money.app)
app.include_router(transact_money.app)
app.include_router(activity_status.app)
app.include_router(borrow_loan.app)
app.include_router(clear_loan.app)
app.include_router(transfer_money.app)