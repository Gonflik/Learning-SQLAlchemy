from models import Song, Album, Artist, Musical_project, Instrument
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session

"-----------------------------------SONG CRUD-------------------------------------------------"
def create_song(session: Session, name: str, length: int, mus_project_id: int, album_id: Optional[int] = None):
    song = Song(name=name,length=length,mus_project_id=mus_project_id,album_id=album_id)
    session.add(song)

def get_song_by_name(session: Session, name: str):
    stmt = select(Song).where(Song.name==name)
    song = session.scalars(stmt).one_or_none()
    return song

def update_song_name(session: Session, new_name: str, song_id: int):
    song = session.get(Song, song_id)
    song.name = new_name

def delete_song(session: Session, song_id: int):
    stmt = select(Song).where(Song.id==song_id)
    song_to_del = session.scalars(stmt).one_or_none()
    if song_to_del:
        session.delete(song_to_del)
    else:
        return False
    
"-------------------------------------------------------------------------------------------------"

"----------------------------------------ARTIST CRUD-----------------------------------------------"
def create_artist(session: Session, name: str, age: Optional[int] = None, gender: Optional[str] = None):
    artist = Artist(name=name, age=age, gender=gender)
    session.add(artist)

def get_artist_by_name(session: Session, name: str):
    stmt = select(Artist).where(Artist.name==name)
    artist = session.scalars(stmt).one_or_none()
    return artist

def update_artist(session: Session,
                artist_id: int ,
                new_name: Optional[str] = None,
                new_age: Optional[int] = None,
                new_gender: Optional[str] = None 
):
    artist = session.get(Artist, artist_id)
    if new_name:
        artist.name = new_name
    elif new_age:
        artist.age = new_age
    elif new_gender:
        artist.gender = new_gender

def delete_artist(session: Session, artist_id: int):
    stmt = select(Artist).where(Artist.id==artist_id)
    artist_to_del = session.scalars(stmt).one_or_none()
    if artist_to_del:
        session.delete(artist_to_del)
    else:
        return False
    
"-----------------------------------------------------------------------------------------------------"

"--------------------------------------MUSICAL_PROJECT CRUD-------------------------------------------"
def create_musical_project(session: Session, 
                           name: str,
                           arist_ids: list[int], 
                           description: Optional[str] = None, 
                           monthly_listens: Optional[int] = None,
                           
):
    mus_project = Musical_project(name=name,description=description,monthly_listens=monthly_listens)

    stmt = select(Artist).where(Artist.id.in_(arist_ids))
    found_artists = session.scalars(stmt).all()

    mus_project.artists.extend(found_artists)

    session.add(mus_project)

def get_musical_project():
    pass



