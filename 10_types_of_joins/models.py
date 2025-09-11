from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from typing import Optional

engine = create_engine('sqlite:///joins.db')



class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return f'< {self.__class__.__name__} id: {self.id}>'


class Address(Base):
    __tablename__ = 'addresses'

    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey('users.id'))
    data: Mapped[str]


class User(Base):
    __tablename__ = 'users'

    first_name: Mapped[str]
    last_name: Mapped[str]
    address: Mapped[Address] = relationship()


# Create the database tables
Base.metadata.create_all(engine)


    
    
    
