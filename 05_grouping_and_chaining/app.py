from models import User,engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()


#Query all user

users = session.query(User).group_by(User.age).all()
print(users)

#To just get the age

users = session.query(User.age).group_by(User.age).all()
print(users)

#How many users in that specific age group

users = session.query(User.age,func.count(User.id)).group_by(User.age).all()
print(users)


#Chaining

users_chain = (session.query(User.age,func.count(User.id))
                             .filter(User.age > 25)
                             .filter(User.age < 50)
                             .order_by(User.age)
                             .group_by(User.age)
                             .all()
                             )

for age,count in users_chain:
        print(f"Age :{age}- {count} users")

