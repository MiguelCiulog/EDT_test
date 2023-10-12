from math import asin, cos, radians, sin, sqrt

from sqlalchemy import select

from src.models.restaurants import Restaurants


class CRUDRestaurants:
    def _haversine(
        self,
        longitude1: float,
        latitude1: float,
        longitude2: float,
        latitude2: float,
    ):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees and meters)

        https://en.wikipedia.org/wiki/Haversine_formula
        """
        # convert decimal degrees to radians
        longitude1, latitude1, longitude2, latitude2 = map(
            radians, [longitude1, latitude1, longitude2, latitude2]
        )

        # haversine formula
        dlon = longitude2 - longitude1
        dlat = latitude2 - latitude1
        a = sin(dlat / 2) ** 2 + cos(latitude1) * cos(latitude2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371000  # Radius of earth in meters.
        return c * r

    def get_restaurants_in_radius(
        self,
        session,
        latitude: float,
        longitude: float,
        radius: float,
    ) -> list[Restaurants]:
        restaurants = session.execute(select(Restaurants)).scalars().all()
        nearby_restaurants = []

        for row in restaurants:
            distance = self._haversine(longitude, latitude, row.lng, row.lat)
            if distance <= radius:
                nearby_restaurants.append(row)

        return nearby_restaurants
