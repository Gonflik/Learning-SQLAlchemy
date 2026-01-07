from models import Artist, Musical_project, Album, Song, Instrument
from database import engine, init_db
from sqlalchemy.orm import Session
import crud

init_db()


with Session(engine) as session:
    crud.create_artist(session, "Gerard Way")
    crud.create_musical_project(session, "Gerard Way", [1], "Solo project")
    crud.create_artist(session, "Ray Toro")
    crud.create_song(session, "Baby youre a haunted house", 166, 1)
    crud.create_musical_project(session, "My Chemical Romance", [1])
    crud.add_member_to_mus_project(session,2,2)
    session.commit()
    

with Session(engine) as sesh:
    crud.read_all_artists_with_projects(sesh)