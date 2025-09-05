from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


db_url="sqlite:///example.db"
engine = create_engine(db_url, echo=True)

Base = declarative_base()

Base.metadata.create_all(engine)
