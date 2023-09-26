from application import db
from application.models import *


db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")

entry1 = User(username ="Robbie", password="jkljkl")

entry2 = Guardian(name = "Robbie", about = "", g_class = "Wizard", attack_type =  "Ranged")
entry3 = Guardian(name = "Duncan", about = "", g_class = "Tank", attack_type = "Melee")
entry4 = Guardian(name = "Alex", about = "", g_class = "Battlemage", attack_type = "Ranged")
entry5 = Guardian(name = "Lanxe", about = "", g_class = "Samurai", attack_type = "Melee")
entry6 = Guardian(name = "Stephanie", about = "", g_class = "Huntress", attack_type ="Melee/Ranged")
entry7 = Guardian(name = "James", about = "", g_class = "Fire Worm", attack_type = "Ranged")

db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6, entry7])

db.session.commit()
