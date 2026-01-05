from models import Artist, Musical_project, Album, Song, Instrument
from database import engine, init_db
from sqlalchemy.orm import Session
import crud

init_db()


with Session(engine) as session:
    crud.create_artist(session, "Gerard Way")
    session.commit()
    print(crud.get_artist_by_name(session, "Gerard Way"))
    crud.create_musical_project(session, "Gerard Way", [1], "Solo project")
    session.commit()
    print(crud.get_musical_project_by_name(session, "Gerard Way"))

    crud.create_artist(session, "Ray Toro")
    session.commit()
    print(crud.get_artist_by_name(session, "Ray Toro"))

    crud.create_song(session, "Baby youre a haunted house", 166, 1)
    session.commit()

    print(crud.get_song_by_name(session, "Baby youre a haunted house"))
    