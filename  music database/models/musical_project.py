from .base import Base
from typing import List
from sqlalchemy import String, ForeignKey 
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Musical_project(Base):
    __table__ = "musical_project"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500))
    monthly_listens: Mapped[int]
    artist_id: Mapped[int] = mapped_column(ForeignKey("artist_info.id"))

    artist: Mapped[List["Artist"]] = relationship(back_populates="musical_project")
    album: Mapped[List["Album"]] = relationship(back_populates="musical_project")
    song: Mapped[List["Song"]] = relationship(back_populates="musical_project")