from application import db
from application.models import Character


db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")

db.session.commit()
