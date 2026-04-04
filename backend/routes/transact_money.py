from fastapi import APIRouter

app = APIRouter()

@app.put("/transact-money")
def transact_money():
    pass