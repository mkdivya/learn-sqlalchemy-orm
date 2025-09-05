import random
from sqlalchemy.orm import sessionmaker
from models import User,engine

Session = sessionmaker(bind=engine)
session = Session()

#Adding multiple data
names = ["alice", "bob", "charlie", "david", "eve", "frank", "grace", "heidi"]
age = [22, 25, 28, 30, 32, 35, 38, 40]

for x in range(20):
        user = User(name=random.choice(names), age=random.choice(age))
        session.add(user)
session.commit()

# Querying and ordering data
users = session.query(User).order_by(User.age).all()
for user in users:
    print(f"Name: {user.name}, Age: {user.age}")