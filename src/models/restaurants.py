from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db import Base


class Restaurants(Base):
    __tablename__ = "restaurants"

    id: Mapped[str] = mapped_column(primary_key=True)
    rating: Mapped[int] = mapped_column(CheckConstraint("rating >= 0 AND rating <= 4"))
    name: Mapped[str]
    site: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    street: Mapped[str]
    city: Mapped[str]
    state: Mapped[str]
    lat: Mapped[float]
    lng: Mapped[float]
