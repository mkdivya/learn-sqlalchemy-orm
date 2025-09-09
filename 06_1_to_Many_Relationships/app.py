from sqlalchemy.orm import sessionmaker
from models import engine, User, Post

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Check if the user already exists
user = session.query(User).filter_by(name="Charlie").first()

# If user doesn't exist, create one
if not user:
    new_user = User(name="Charlie", age=28)
    new_user.posts = [
        Post(title="Mapped Post 1"),
        Post(title="Mapped Post 2")
    ]
    session.add(new_user)
    session.commit()
    user = new_user  # assign newly created user

# Display user info
print(f"User: {user.name}, Age: {user.age}")

# Display posts
for post in user.posts:
    print(f"- Post: {post.title}")
