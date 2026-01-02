from sqlalchemy import Table, Column, ForeignKey
from .base import Base

artist_instrument_association = Table(
    "artist_instrument_association",
     Base.metadata,
    Column("artist_id", ForeignKey("artist_info.id")),
    Column("instrument_id", ForeignKey("instrument.id"))
) 
