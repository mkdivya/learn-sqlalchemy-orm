from models import User,engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


#Query all user

all_users = session.query(User).all()

#query to get all users age >30
#filter doesnt take args directly like age u have to pass it like User.age>30 only

# users_filtered =(session.query(User).filter(User.age > 30).all()) 
# for u in users_filtered:
#     print(u.name,u.age)

#Using multiple conditions

# users = session.query(User).filter(User.age > 25, User.name.like("C%")).all()
# for u in users:
#     print(u.name,u.age)

