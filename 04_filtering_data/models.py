from sqlalchemy import URL, create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


db_url="sqlite:///example.db"
engine = create_engine(db_url, echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self) -> str:
        return f'<User id: {self.id:>3}: name: {self.name:<13}, age: {self.age:>3}>'




Base.metadata.create_all(engine)
