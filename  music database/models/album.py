from .base import Base
from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Album(Base):
    __tablename__ = "album"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    length: Mapped[int] = 0
    mus_project_id: Mapped[int] = mapped_column(ForeignKey("musical_project.id"))

    musical_project: Mapped["Musical_project"] = relationship(back_populates="albums")
    songs: Mapped[List["Song"]] = relationship(back_populates="album")

    def __repr__(self):
        return f"<{self.__class__} name: {self.name}, id: {self.id}, lentgh: {self.length}, mus_project_id: {self.mus_project_id}>"