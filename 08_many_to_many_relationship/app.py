from models import Student, Course, session

# 1️⃣ Create students
alice = Student(name="Alice")
bob = Student(name="Bob")

# 2️⃣ Create courses
math = Course(title="Math")
physics = Course(title="Physics")

# 3️⃣ Enroll students in courses
alice.courses = [math, physics]  # Alice takes Math and Physics
bob.courses = [physics]          # Bob takes Physics

# 4️⃣ Add to session and commit
session.add_all([alice, bob])
session.commit()

# ✅ Check relationships
print(f"Alice's courses: {[c.title for c in alice.courses]}")
print(f"Bob's courses: {[c.title for c in bob.courses]}")
print(f"Students in Physics: {[s.name for s in physics.students]}")
