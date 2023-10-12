import statistics

from fastapi import APIRouter, Depends, HTTPException, status

from src.core.db import get_database_session
from src.crud.restaurants import CRUDRestaurants
from src.schemas.restaurants import RestaurantsOutput

router = APIRouter(prefix="/restaurants", tags=["restaurant"])


@router.get(
    "/statistics",
    response_model=RestaurantsOutput,
    status_code=status.HTTP_200_OK,
    summary="Returns statistics about all the restaurants near the area in the radius",
    description="Returns count, average and standard deviation about all the restaurants near the the latitude and longitude around the radius.",
)
async def get_restaurants_in_radius(
    latitude: float,
    longitude: float,
    radius: float,
    session=Depends(get_database_session),
) -> RestaurantsOutput:
    restaurants = CRUDRestaurants().get_restaurants_in_radius(
        session,
        latitude,
        longitude,
        radius,
    )
    count = len(restaurants)
    if count == 0:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"No restaurants found on radius: {radius}, latitude: {latitude}, longitude: {longitude}",
        )
    if count == 1:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Only 1 restaurant found on radius: {radius}, latitude: {latitude}, longitude: {longitude}",
        )

    ratings = [x.rating for x in restaurants]
    mean = statistics.mean(ratings)
    std = statistics.stdev(ratings, mean)

    res = RestaurantsOutput(count=count, avg=mean, std=std)
    return res
