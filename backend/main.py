from fastapi import FastAPI
from routes import (
    home, 
    get_all_users, 
    get_user_by_pin, 
    create_account, 
    update_account_details, 
    delete_account,
    deposit_money,
    transact_money
)

app = FastAPI()

app.include_router(home.app)
app.include_router(get_all_users.app)
app.include_router(get_user_by_pin.app)
app.include_router(create_account.app)
app.include_router(update_account_details.app)
app.include_router(delete_account.app)
app.include_router(deposit_money.app)
app.include_router(transact_money.app)