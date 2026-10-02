from fastapi import FastAPI
from routes import (
    home
)

# INITIALIZING APP
app = FastAPI(
    title="Banking System",
    description="A Complete FastAPI driven Banking System Backend",
    version="1.0.0"
)

# INCLUDING ROUTERS
app.include_router(home.router)