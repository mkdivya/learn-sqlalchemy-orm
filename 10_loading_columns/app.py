from sqlalchemy.orm import sessionmaker, undefer, raiseload, noload
from models import User, Article, Post, engine

Session = sessionmaker(bind=engine)
session = Session()

# --- Create sample data ---
user = User(name="Alice")
article = Article(title="Deferred Example", content="Very big content " * 1000)
post = Post(content="Post Content Example", user=user)

session.add_all([user, article, post])
session.commit()

# --- Example 1: deferred column (content is not loaded by default) ---
print("\n👉 Example 1: deferred column (content is lazy-loaded)")
article_obj = session.query(Article).first()
print(article_obj.title)  # No extra query yet
print(article_obj.content)  # Now triggers a separate SELECT query

# --- Example 2: undefer column (force loading immediately) ---
print("\n👉 Example 2: undefer column (content is loaded immediately)")
article_obj2 = session.query(Article).options(undefer(Article.content)).first()
print(article_obj2.title)
print(article_obj2.content)  # Content already loaded in same query

# --- Example 3: raiseload (prevent lazy-loading of relationship) ---
print("\n👉 Example 3: raiseload (raises error if accessed)")
post_obj = session.query(Post).options(raiseload(Post.user)).first()
print(post_obj.content)
try:
    print(post_obj.user.name)  # Raises an error
except Exception as e:
    print(f"Error: {e}")

# --- Example 4: noload (relationship is never loaded, returns None) ---
print("\n👉 Example 4: noload (relationship is not loaded, returns None)")
post_obj2 = session.query(Post).options(noload(Post.user)).first()
print(post_obj2.content)
print(post_obj2.user)  # Prints None, no additional query
