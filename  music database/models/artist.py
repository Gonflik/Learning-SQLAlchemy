from .base import Base
from .associations.artist_proj_association import artist_proj_association
from .associations.artist_instrument_association import artist_instrument_association
from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Artist(Base):
    __tablename__ = "artist_info"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[Optional[int]]
    gender: Mapped[Optional[str]]
    
    musical_projects: Mapped[List["Musical_project"]] = relationship(
        secondary=artist_proj_association,
        back_populates="artists"
    )
    instruments: Mapped[Optional[List["Instrument"]]] = relationship(
        secondary=artist_instrument_association,
        back_populates="artists"
    )

    def __repr__(self):
        return f"<{self.__class__} name: {self.name}, id: {self.id}, age: {self.age}, gender: {self.gender}>"
    