import sqlalchemy
from typing import List
from sqlalchemy import String,Text, create_engine, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship, Session

engine = create_engine("sqlite://", echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))

    posts: Mapped[List["Post"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    comments: Mapped[List["Comment"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id: {self.id}, name: {self.name})"

class Post(Base):
    __tablename__ = "user_post"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    title: Mapped[str] = mapped_column(default="Untitled")
    text: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")

    def __repr__(self):
        return f"Post(id: {self.id}, user_id: {self.user_id}, title: {self.title}, text: {self.text})"
    
class Comment(Base):
    __tablename__ = "user_comment"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("user_post.id"))
    text: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship(back_populates="comments")
    post: Mapped["Post"] = relationship(back_populates="comments")

    def __repr__(self):
        return f"Comment(id: {self.id!r}, user_id: {self.user_id!r}, post_id: {self.post_id!r}, text: {self.text!r})"

Base.metadata.create_all(engine)

def create_user(session: Session,name: str):
    user = User(name=name)
    session.add(user)

def read_user(session: Session,user_id: int):
    stmt = select(User).where(User.id == user_id)
    print(session.scalars(stmt).one_or_none())

def update_username(session: Session,new_name: str, user_id: int):
    """
    get_user = select(User).where(User.id == user_id)
    user = session.scalars(get_user)
    user.name = new_name
    #якшо шукати по PK то можна юзати get() замість select() ,а потім  scalars()
    """
    user = session.get(User, user_id)
    if user:
        user.name = new_name
    else:
        print(f"Error: User with ID {user_id} not found.")

def delete_user(session: Session,user_id: int):
    stmt = select(User).where(User.id == user_id)
    user_to_del = session.scalars(stmt).one_or_none()
    if user_to_del:
        session.delete(user_to_del)
    else:
        print(f"Deletion failed! No user with id: {user_id}")

with Session(engine) as session:
    create_user(session,"Bob")
    session.commit()

    read_user(session, 1)
    update_username(session, "Bob-cao",1)
    session.commit()

    read_user(session, 1)
    delete_user(session, 1)
    session.commit()