from application import db
from application.models import User


db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")

entry1 = User(username ="Robbie", email="robbie@example.com", password="jkljkl")

db.session.add(entry1)

db.session.commit()
