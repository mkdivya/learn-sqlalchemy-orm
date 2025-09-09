from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
#(for non-mapped)
# from sqlalchemy.orm import declarative_base,relationship 
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

db_url = "sqlite:///relationship1.db"
engine = create_engine(db_url)

#(for non-mapped)
# Base = declarative_base() 

#for mapped

class Base(DeclarativeBase):
        pass


#User model for non-mapped

class User(Base):
        __tablename__ = "users"
        id = Column(Integer,primary_key=True)
        name = Column(String)
        age = Column(Integer)

        #one to many relationship
        posts = relationship("Post",back_populates="user")

        def __repr__(self) -> str:
                return f"<User id:{self.id} name:{self.name} age:{self.age}>"

#User model for mapped
class User(Base):
        __tablename__ = "users"
        id:Mapped[int]=mapped_column(primary_key = True)
        name = Mapped[str]
        age = Mapped[int]

        #1 to many relationship
        posts : Mapped[list["Post"]]=relationship(back_populates="user",cascade="all, delete")

        def __repr__(self) -> str:
                return f"<User id:{self.id} name:{self.name} age:{self.age}>"

        
#Post model for non-mapped

class Post(Base):
        __tablename__ = "posts"
        id = Column(Integer,primary_key=True)
        title = Column(String)
        user_id = Column(Integer,ForeignKey("users.id"))

        #referece back to the user
        user = relationship("User",back_populates="posts")

        def __repr__(self) -> str:
                return f"<Post id:{self.id} title:{self.title} user_id:{self.user_id}>"


#Post model for mapped

class Post(Base):
        __tablename__= "posts"
        id:Mapped[int]=mapped_column(primary_key=True)
        title:Mapped[str]
        user_id:Mapped[int]=mapped_column(ForeignKey("users.id"))

        user :Mapped["User"]=relationship(back_populates="posts")

        def __repr__(self) -> str:
                return f"<Post id:{self.id} title:{self.title} user_id:{self.user_id}>"
        
Base.metadata.create_all(engine)
