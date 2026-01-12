from models import Artist, Musical_project, Album, Song, Instrument
from models.database import engine, init_db
from sqlalchemy.orm import Session
import controller.crud as crud

init_db()


with Session(engine) as session:
    crud.create_artist(session, "Gerard Way")
    crud.create_musical_project(session, "Gerard Way", [1], "Solo project")
    crud.create_artist(session, "Ray Toro")
    crud.create_song(session, "Baby youre a haunted house", 166, 1)
    crud.create_musical_project(session, "My Chemical Romance", [1])
    crud.add_member_to_mus_project(session,2,2)
    session.commit()

with Session(engine) as session:
    crud.create_album(session, "Three cheers for sweet revenge", 2)
    crud.create_song(session, "Helena", 205, 2, 1)
    crud.create_song(session, "Give 'Em Hell, Kid", 139, 2, 1)
    crud.create_song(session, "To the End", 182, 2, 1)
    crud.create_song(session, "You Know What They Do To Guys Like Us in Prison", 174, 2, 1)
    session.commit()

with Session(engine) as sesh:
    crud.read_all_artists_with_projects(sesh)
    crud.read_album_by_name(session, "Three cheers for sweet revenge")
    crud.add_songs_to_album(session, [1], 1)
    crud.read_album_with_songs_by_name_selectinload(session, "Three cheers for sweet revenge")
    crud.delete_song_by_id(session, 1)
    session.commit()
    crud.read_album_with_songs_by_name_selectinload(session, "Three cheers for sweet revenge")