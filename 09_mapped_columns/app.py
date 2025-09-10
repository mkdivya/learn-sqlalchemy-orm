from models import User,engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Divya",age=22)
session.add(new_user)
session.commit()

users = session.query(User).all()

for user in users:
        print(user)


session.close()