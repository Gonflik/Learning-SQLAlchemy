from database import init_db, engine
import crud
from sqlalchemy.orm import Session
from models import User, Post, Comment

init_db()

with Session(engine) as session:
    crud.create_user(session,"Bob")
    session.commit()

    crud.create_post(session, 1, "Bebroski", "lorempisum loremipsum bababababababababaabab")
    session.commit()

    crud.create_comment(session, 1, 1, "Boze chel watafa fafafa")
    session.commit()

    crud.read_user(session, 1)
    crud.update_username(session, "Bob-cao",1)
    session.commit()

    crud.read_user(session, 1)
    crud.delete_user(session, 1)
    session.commit()

    crud.read_user(session, 1)

