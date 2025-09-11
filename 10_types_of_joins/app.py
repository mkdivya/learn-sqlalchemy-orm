from sqlalchemy.orm import sessionmaker
from models import User, Address,engine

Session = sessionmaker(bind=engine)
session = Session()


if session.query(User).count() < 1:
    # This address IS used
    address_1 = Address(data='1234 Random Address')

    # These addresses are NOT used
    address_2 = Address(data='5678 Non-existant Address')
    address_3 = Address(data='9012 Extra Address')

    # User with an address
    user_1 = User(
        first_name='Zeq',
        last_name='Tech',
        address=address_1,
    )

    # User without an address
    user_2 = User(
        first_name='Banana',
        last_name='Man',
        address=None,
    )

    session.add_all([address_1, address_2, address_3, user_1, user_2])
    session.commit()

# --- INNER JOIN ---

result = session.query(User).join(Address).all()
print('\nINNER JOIN')
print(result)

# --- LEFT OUTER JOIN ---
result = session.query(User).outerjoin(Address).all()
print('\nLEFT OUTER JOIN')
print(result)

# --- RIGHT OUTER JOIN ---
result = session.query(Address,User).outerjoin(User).all()
print('\nRIGHT OUTER JOIN')
print(result)

# --- FULL OUTER JOIN ---
left_join = session.query(User, Address).outerjoin(Address)  # Gets all Users
right_join = session.query(User, Address).outerjoin(User)  # Gets all Addresses
full_outer_join = left_join.union(right_join)
print('\nFULL JOIN')
print(full_outer_join.all())
