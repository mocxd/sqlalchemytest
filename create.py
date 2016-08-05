from sqlalchemy import create_engine
from model import Base

engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)