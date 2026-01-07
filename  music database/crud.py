from models import Song, Album, Artist, Musical_project, Instrument
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

"-----------------------------------SONG CRUD-------------------------------------------------"
def create_song(session: Session, name: str, length: int, mus_project_id: int, album_id: Optional[int] = None):
    song = Song(name=name,length=length,mus_project_id=mus_project_id,album_id=album_id)
    session.add(song)

def get_song_by_name(session: Session, name: str):
    stmt = select(Song).where(Song.name==name)
    song = session.scalars(stmt).one_or_none()
    return song

def get_song_by_id(session: Session, song_id: int):
    song = session.get(Song, song_id)
    return song

def read_song_by_name(session: Session, name: str):
    song = get_song_by_name(session, name)
    if song:
        print(song)
    else:
        print(f"Song: {name} not found.")

def update_song_name_by_id(session: Session, new_name: str, song_id: int):
    song = session.get(Song, song_id)
    song.name = new_name

def add_songs_to_album(session: Session, song_ids: list[int], album_id: int):
    album = session.get(Album, album_id)

    stmt = select(Song).where(Song.id.in_(song_ids))
    found_songs = session.scalars(stmt).all()
    
    album.songs.extend(found_songs)

def delete_song_by_id(session: Session, song_id: int):
    song_to_del = session.get(Song, song_id)
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

def get_artist_by_id(session: Session, artist_id: int):
    artist = session.get(Artist, artist_id)
    return artist

def read_artist_by_name(session: Session, name: str):
    artist = get_artist_by_name(session, name)
    if artist:
        print(artist)
    else:
        print(f"Artist: {name} not found.")

def read_all_artists(session: Session):
    stmt = select(Artist).order_by(Artist.name)
    artists = session.scalars(stmt).all()
    if artists:
        for artist in artists:
            print(artist)
    else:
        print("No artists in DB.")

def read_all_artists_with_projects(session: Session):
    stmt = select(Artist).options(selectinload(Artist.musical_projects)).order_by(Artist.name)
    artists = session.scalars(stmt).all()
    print(50*"-")
    for artist in artists:
        print(artist)
        for project in artist.musical_projects:
            print(f"{artist.name} projects", project)
        print(50*"-")

def update_artist_by_id(session: Session,
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

def delete_artist_by_id(session: Session, artist_id: int):
    artist_to_del = session.get(Artist, artist_id)
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

def get_musical_project_by_id(session: Session, mus_proj_id: int):
    mus_proj = session.get(Musical_project, mus_proj_id)
    return mus_proj

def read_musical_project_by_name(session: Session, name: str):
    mus_proj = get_musical_project_by_name(session, name)
    if mus_proj:
        print(mus_proj)
    else:
        print(f"Musical project: {name} not found.")

def add_member_to_mus_project(session: Session, mus_project_id: int, artist_id: int):
    mus_project = session.get(Musical_project, mus_project_id)
    artist = session.get(Artist, artist_id)

    if mus_project and artist:
        mus_project.artists.append(artist)
    else:
        return False

def delete_mus_project_by_id(session: Session, mus_proj_id: int):
    mus = session.get(Musical_project, mus_proj_id)
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
    if album:
        print(album)
    else:
        print(f"Album: {name} not found.")

def update_album_name_by_id(session: Session, album_id: int, new_name: str):
    album = session.get(Album, album_id)
    if album:
        album.name = new_name
    else:
        return False
    
def delete_album_by_id(session: Session, album_id: int):
    album = session.get(Album, album_id)
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
    instrument =  session.get(Instrument, instrument_id)
    return instrument

def read_instrument_by_name(session: Session, name: str):
    instrument = get_instrument_by_name(session, name)
    if instrument:
        print(instrument)
    else:
        print(f"Instrument: {name} not found.")

def update_instrument_name_by_name(session: Session, old_name: str, new_name: str):
    instrument = get_instrument_by_name(session, old_name)
    if instrument:
        instrument.name = new_name
    else:
        return False
    
def delete_instrument_by_id(session: Session, instrument_id: int):
    instrument = session.get(Instrument, instrument_id)
    if instrument:
        session.delete(instrument)
    else:
        return False
