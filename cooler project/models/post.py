from .base import Base
from typing import List
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship



class Post(Base):
    __tablename__ = "user_post"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    title: Mapped[str] = mapped_column(default="Untitled")
    text: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")

    def __repr__(self):
        return f"Post(id: {self.id}, user_id: {self.user_id}, title: {self.title}, text: {self.text[:10]}...)"
                