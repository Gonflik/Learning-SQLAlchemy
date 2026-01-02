from .base import Base
from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Album(Base):
    __table__ = "album"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    length: Mapped[int]
    mus_project_id: Mapped[int] = mapped_column(ForeignKey("musical_project.id"))

    musical_project: Mapped["Musical_project"] = relationship(back_populates="album")
    songs: Mapped[List["Songs"]] = relationship(back_populates="album")