from fastapi import FastAPI
from routes import (
    home
)

# Initializing App
app = FastAPI(
    title="Banking System - FastAPI"
)

# Including Routers
app.include_router(home.router)