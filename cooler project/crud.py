from models import User, Post, Comment
from sqlalchemy import select
from sqlalchemy.orm import Session

def create_user(session: Session,name: str):
    user = User(name=name)
    session.add(user)

def create_post(session: Session, user_id: int, title: str, text: str):
    post  = Post(user_id=user_id,title=title,text=text)
    session.add(post)

def create_comment(session: Session, user_id: int, post_id: int, text: str):
    comment = Comment(user_id=user_id, post_id=post_id, text=text)
    session.add(comment)

def read_user(session: Session,user_id: int):
    stmt = select(User).where(User.id == user_id)
    print(session.scalars(stmt).one_or_none())


def update_username(session: Session,new_name: str, user_id: int):
    user = session.get(User, user_id)
    user.name = new_name

def delete_user(session: Session,user_id: int):
    stmt = select(User).where(User.id == user_id)
    user_to_del = session.scalars(stmt).one_or_none()
    if user_to_del:
        session.delete(user_to_del)
    else:
        print(f"Deletion failed! No user with id: {user_id}")