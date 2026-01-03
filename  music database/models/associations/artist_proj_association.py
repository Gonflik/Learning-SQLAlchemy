from sqlalchemy import Table, Column, ForeignKey
from ..base import Base

artist_proj_association = Table(
    "artist_proj_association",
     Base.metadata,
    Column("artist_id", ForeignKey("artist_info.id")),
    Column("musical_project_id", ForeignKey("musical_project.id"))
) 
