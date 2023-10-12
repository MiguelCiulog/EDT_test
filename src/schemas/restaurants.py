from pydantic import BaseModel


class RestaurantsOutput(BaseModel):
    count: int
    avg: float
    std: float
