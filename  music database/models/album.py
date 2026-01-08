from .base import Base
from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Album(Base):
    __tablename__ = "album"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    length: Mapped[int] = mapped_column(default=0)
    mus_project_id: Mapped[int] = mapped_column(ForeignKey("musical_project.id"))

    musical_project: Mapped["Musical_project"] = relationship(back_populates="albums")
    songs: Mapped[List["Song"]] = relationship(back_populates="album")

    def recalculate_length(self, session: "Session"):
        from sqlalchemy import func
        from .song import Song
        new_length = session.query(func.sum(Song.length)).filter(Song.album_id==self.id).scalar()
        if new_length is not None:
            self.length = new_length
        else:
            self.length = 0
        

    def __repr__(self):
        return f"<{self.__class__} name: {self.name}, id: {self.id}, lentgh: {self.length}, mus_project_id: {self.mus_project_id}>"