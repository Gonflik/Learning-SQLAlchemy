from .base import Base
from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Song(Base):
    __table__ = "song"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    length: Mapped[int]

    mus_project_id: Mapped[int] = mapped_column(ForeignKey("musical_project.id"))
    album_id: Mapped[Optional[int]] = mapped_column(ForeignKey("album.id"))

    musical_project: Mapped["Musical_project"] = relationship(back_populates="songs")
    album: Mapped[Optional["Album"]] = relationship(back_populates="songs")

    def __repr__(self):
        return f"Song(name: {self.name}, id: {self.id}, lentgh: {self.length}, album_id: {self.album_id})"