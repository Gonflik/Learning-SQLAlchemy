from .base import Base
from .artist_instrument_association import artist_instrument_association
from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Instrument(Base):
    __table__ = "instrument"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    
    artist: Mapped[List["Artist"]] = relationship(
        secondary=artist_instrument_association,
        back_populates="instruments"
    )