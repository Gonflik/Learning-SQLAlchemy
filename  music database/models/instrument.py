from .base import Base
from .associations.artist_instrument_association import artist_instrument_association
from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Instrument(Base):
    __tablename__ = "instrument"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    
    artists: Mapped[Optional[List["Artist"]]] = relationship(
        secondary=artist_instrument_association,
        back_populates="instruments"
    )

    def __repr__(self):
        return f"<{self.__class__} name: {self.name}, id: {self.id}>"