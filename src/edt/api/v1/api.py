from fastapi import APIRouter

from api.v1.endpoints import restaurants

api_router = APIRouter(prefix="/v1")
api_router.include_router(restaurants.router)
