from application import db
from application.models import Guardian


db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")

# entry1 = User(username ="Robbie", email="robbie@example.com", password="jkljkl")

entry2 = Guardian(name = "Robbie", about = "", g_class = "Wizard", attack_type =  "Ranged", sprite = "")
entry3 = Guardian(name = "Duncan", about = "", g_class = "Tank", attack_type = "Melee", sprite = "https://img.itch.zone/aW1hZ2UvODcwNzM2LzQ5NTQ3OTUuZ2lm/347x500/DrPiFO.gif")
entry4 = Guardian(name = "Alex", about = "", g_class = "Battlemage", attack_type = "Ranged", sprite = "https://img.itch.zone/aW1hZ2UvODUwMzk1LzQ4Mjg0MDcuZ2lm/347x500/Y%2BWq2Z.gif")
entry5 = Guardian(name = "Lanxe", about = "", g_class = "Samurai", attack_type = "Melee", sprite = "https://img.itch.zone/aW1hZ2UvNjU4NzA0LzM1NDUxNDYuZ2lm/347x500/zEoWaW.gif")
entry6 = Guardian(name = "Stephanie", about = "", g_class = "Huntress", attack_type ="Melee/Ranged", sprite = "https://img.itch.zone/aW1hZ2UvNzkyNzYzLzQ0NjU4NTAuZ2lm/347x500/Uvw4IK.gif")
entry7 = Guardian(name = "James", about = "", g_class = "Fire Worm", attack_type = "Ranged", sprite = "https://img.itch.zone/aW1hZ2UvODk0MTAyLzUwNjIxNzYuZ2lm/347x500/1Wt4f5.gif")

db.session.add_all([entry2, entry3, entry4, entry5, entry6, entry7])

db.session.commit()
