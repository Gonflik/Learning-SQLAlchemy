from .base import Base
from .associations.artist_proj_association import artist_proj_association
from typing import List, Optional
from sqlalchemy import String, ForeignKey 
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Musical_project(Base):
    __tablename__ = "musical_project"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(500))
    monthly_listens: Mapped[int] = mapped_column(default=0)

    artists: Mapped[List["Artist"]] = relationship(
        secondary=artist_proj_association,
        back_populates="musical_projects"
    )
    albums: Mapped[Optional[List["Album"]]] = relationship(back_populates="musical_project")
    songs: Mapped[Optional[List["Song"]]] = relationship(back_populates="musical_project")

    def __repr__(self):
        return f"<{self.__class__} name: {self.name}, id: {self.id}>"