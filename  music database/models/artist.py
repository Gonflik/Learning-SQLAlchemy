from .base import Base
from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Artist(Base):
    __table__ = "artist_info"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]
    gender: Mapped[str] = mapped_column(nullable=True)
    
    instruments: Mapped[List["Instrument"]] = relationship(back_populates="artist")
    