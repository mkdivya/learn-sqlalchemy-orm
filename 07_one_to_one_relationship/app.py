from models import User, Address, session

# 1️⃣ Create a new user
alice = User(name="Alice")

# 2️⃣ Create a new address
alice_home = Address(email="alice@example.com")

# 3️⃣ Link them (one-to-one)
alice.address = alice_home

# 4️⃣ Add to session and commit
session.add(alice)
session.commit()

# ✅ Check relationships
print(f"User: {alice.name}")
print(f"Address of user: {alice.address.email}")
print(f"Back from address: {alice_home.user.name}")
