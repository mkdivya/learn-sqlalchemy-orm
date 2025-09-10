from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, deferred

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = deferred(Column(Text))  # Deferred: Will not load by default

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")  # Relationship to user

# Database engine
engine = create_engine('sqlite:///test.db', echo=True)

# Create tables
Base.metadata.create_all(engine)
