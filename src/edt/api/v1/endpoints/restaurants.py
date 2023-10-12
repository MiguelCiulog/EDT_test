from fastapi import APIRouter

router = APIRouter(prefix="/restaurants", tags=["restaurant"])


@router.get("/statistics/")
async def get_restaurants_in_radius(latitude: float, longitude: float, radius: float):
    return {"latitude": latitude, "longitude": longitude, "radius": radius}
