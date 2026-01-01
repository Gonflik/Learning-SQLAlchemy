from .base import Base
from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Album(Base):
    __table__ = "album"
    pass