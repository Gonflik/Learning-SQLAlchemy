from .base import Base
from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Instrument(Base):
    __table__ = "instrument"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    
    #artist_id: Mapped[int] = mapped_column(ForeignKey("artist_info.id"))
    #artist: Mapped["Artist"] = relationship(back_populates="instrument") тре мені ту мені делать походу