from .base import Base
from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))

    posts: Mapped[List["Post"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    comments: Mapped[List["Comment"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"{'#'*40} \nUser(id: {self.id}, name: {self.name}) \nPosts: {len(self.posts)},Comments: {len(self.comments)}\n{'#'*40}"
