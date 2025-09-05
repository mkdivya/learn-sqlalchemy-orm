from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

#add single user to db
user = User(name= "alice",age=30)
session.add(user)
session.commit()

#add multiple users to db
user1 = User(name= "bob",age=25)
user2 = User(name= "charlie",age=35)    
user3 = User(name= "david",age=28)
user4 = User(name= "eve",age=22)

session.add_all([user1,user2,user3,user4])
session.commit()


#db query

user = session.query(User).all()
users = user[0]
print(users)
print(users.id)
print(users.name)
print(users.age)

for users in user:
        print(f"User Id: {users.id}, User Name: {users.name}, User Age: {users.age}")


#db quert with filter

user = session.query(User).filter_by(id=1).first()
print(user)
print(user.id)
print(user.name)
print(user.age)

user.name = "alice-updated"
session.commit()

#delete 

user = session.query(User).filter_by(id=1).first()
session.delete(user)
session.commit()