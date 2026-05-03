from fastapi import FastAPI
app = FastAPI()

from routes import (
    borrow_loan,
    clear_loan,
    create_account,
    delete_account,
    update_account,
    deposit_money,
    get_all_users,
    get_individual_user,
    home,
    withdraw_money,
    transfer_money
)

app.include_router(home.app)
app.include_router(get_all_users.app)
app.include_router(get_individual_user.app)
app.include_router(create_account.app)
app.include_router(delete_account.app)
app.include_router(update_account.app)
app.include_router(deposit_money.app)
app.include_router(withdraw_money.app)
app.include_router(borrow_loan.app)
app.include_router(clear_loan.app)
app.include_router(transfer_money.app)