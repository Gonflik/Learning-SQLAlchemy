from .base import Base
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Comment(Base):
    __tablename__ = "user_comment"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("user_post.id"))
    text: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship(back_populates="comments")
    post: Mapped["Post"] = relationship(back_populates="comments")

    def __repr__(self):
        return f"{self.user.name}: {self.text[:10]}... \n(id: {self.id!r}, user_id: {self.user_id!r}, post_id: {self.post_id!r}, text: {self.text!r})"
