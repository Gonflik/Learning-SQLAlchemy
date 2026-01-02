from sqlalchemy import create_engine
from models import Base

engine = create_engine("sqlite://")

def init_db():
    Base.metadata.create_all(engine)