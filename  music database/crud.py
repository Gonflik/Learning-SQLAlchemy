from models import Song, Album, Artist, Musical_project, Instrument
from sqlalchemy import select
from sqlalchemy.orm import Session

def create_song(session: Session, name: str, length: int, mus_project_id: int, album_id: int):
    song = Song(name=name,length=length,mus_project_id=mus_project_id,album_id=album_id)
    session.add(song)

def get_song_by_name(session: Session, name: str):
    stmt = select(Song).where(Song.name==name)
    song = session.scalars(stmt).one_or_none()
    return song


