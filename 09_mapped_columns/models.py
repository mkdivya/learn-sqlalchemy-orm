from sqlalchemy import String,Integer,create_engine
#Imports
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
#mapped_column is used to define the column properties its used in modern approach its similar to column function but recommended in new projects.
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age:Mapped[int]=mapped_column(default=18)


    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, age={self.age!r})"
    
DATABASE_URL = "sqlite+pysqlite:///./mapped.db"
engine = create_engine(DATABASE_URL,echo = True)

Base.metadata.create_all(engine)
