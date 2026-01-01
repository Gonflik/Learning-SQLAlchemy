from .base import Base
from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Song(Base):
    __table__ = "song"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    length: Mapped[int]

    mus_project_id: Mapped[int] = mapped_column(ForeignKey("musical_project.id"))
    album_id: Mapped[int] = mapped_column(ForeignKey("album.id"))