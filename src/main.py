from fastapi import FastAPI
from .routes import register_routes

app = FastAPI()

def bootstrap():
    # Initialize routes
    app.include_router(register_routes())


bootstrap()