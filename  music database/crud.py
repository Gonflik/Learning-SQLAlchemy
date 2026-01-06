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

def read_song_by_name(session: Session, name: str):
    song = get_song_by_name(session, name)
    print(song)

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

def read_artist_by_name(session: Session, name: str):
    artist = get_artist_by_name(session, name)
    print(artist)

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
                           monthly_listens: Optional[int] = None
                           
):
    mus_project = Musical_project(name=name,description=description,monthly_listens=monthly_listens)

    stmt = select(Artist).where(Artist.id.in_(arist_ids))
    found_artists = session.scalars(stmt).all()

    mus_project.artists.extend(found_artists)

    session.add(mus_project)

def get_musical_project_by_name(session: Session, name: str):
    stmt = select(Musical_project).where(Musical_project.name==name)
    mus_project = session.scalars(stmt).one_or_none()
    return mus_project

def read_musical_project_by_name(session: Session, name: str):
    mus_proj = get_musical_project_by_name(session, name)
    print(mus_proj)

def add_member_to_mus_project(session: Session, mus_project_id: int, artist_id: int):
    mus_project = session.get(Musical_project, mus_project_id)
    artist = session.get(Artist, artist_id)

    if mus_project and artist:
        mus_project.artists.append(artist)
    else:
        return False

def delete_mus_project(session: Session, name: str):
    mus = get_musical_project_by_name(name)
    if mus:
        session.delete(mus)
    else:
        return False

"---------------------------------------------ALBUM CRUD-------------------------------------------------"
def create_album(session: Session, name: str, mus_project: id):
    album = Album(name=name,mus_project=mus_project)
    session.add(album)

def get_album_by_id(session: Session, album_id: int):
    album = session.get(Album, album_id)
    return album

def get_album_by_name(session: Session, name: str):
    stmt = select(Album).where(Album.name==name)
    album = session.scalars(stmt).one_or_none
    return album

def read_album_by_name(session: Session, name: str):
    album = get_album_by_name(session, name)
    print(album)

def update_album_name_by_id(session: Session, album_id: int, new_name: str):
    album = get_album_by_id(session, album_id)
    if album:
        album.name = new_name
    else:
        return False
    
def delete_album_by_id(session: Session, album_id: int):
    album = get_album_by_id(session, album_id)
    if album:
        session.delete(album)
    else:
        return False
    
"-------------------------------------------------INSTRUMENT CRUD--------------------------------------------"
def create_instrument(session: Session, name: str):
    instrument = Instrument(name=name)
    session.add(instrument)

def get_instrument_by_name(session: Session, name: str):
    stmt = select(Instrument).where(Instrument.name==name)
    instrument = session.scalars(stmt).one_or_none()
    return instrument

def get_instrument_by_id(session: Session, instrument_id: int):
    stmt = select(Instrument).where(Instrument.id==instrument_id)
    instrument = session.scalars(stmt).one_or_none()
    return instrument

def read_instrument_by_name(session: Session, name: str):
    instrument = get_instrument_by_name(session, name)
    print(instrument)

def update_instrument_name_by_name(session: Session, old_name: str, new_name: str):
    instrument = get_instrument_by_name(session, old_name)
    if instrument:
        instrument.name = new_name
    else:
        return False
    
def delete_instrument_by_id(session: Session, instrument_id: int):
    instrument = get_instrument_by_id(session, instrument_id)
    if instrument:
        session.delete(instrument)
    else:
        return False
