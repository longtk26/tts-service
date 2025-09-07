from fastapi import APIRouter
from src.modules.media import media_route


app_routes = [media_route]

def register_routes():
    main_routes = APIRouter()

    for route in app_routes:
        main_routes.include_router(route)

    return main_routes