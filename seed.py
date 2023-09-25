from application import db
from application.models import Character


db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")

# entry1 = User(username ="Robbie", email="robbie@example.com", password="jkljkl")

entry2 = Character(name = "Robbie", c_class = "Wizard", attack_type =  "Ranged")
entry3 = Character(name = "Duncan", c_class = "Tank", attack_type = "Melee")
entry4 = Character(name = "Alex", c_class = "Battlemage", attack_type = "Ranged")
entry5 = Character(name = "Lanxe", c_class = "Samurai", attack_type = "Melee")
entry6 = Character(name = "Stephanie", c_class = "Huntress", attack_type ="Melee/Ranged")
entry7 = Character(name = "James", c_class = "Fire Worm", attack_type = "Ranged")

db.session.add_all([entry2, entry3, entry4, entry5, entry6, entry7])

db.session.commit()
