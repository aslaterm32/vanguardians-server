from application import db
from application.models import *


db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")

entry1 = User(username="Robbie", password="jkljkl")

entry2 = Guardian(
    name="Robbie",
    about="A wise and weathered wizard, hails from a lineage of time-bending mages. His staff crackles with the energy of the ages, and with a mere gesture, he can call upon the fury of the skies. His eyes hold the weight of centuries, and his purpose is clear - protect the time-traveling vehicle at all costs, for the threads of time must not unravel.", 
    g_class="Wizard", 
    attack_type="Ranged", 
    mode_1="Calls an AOE lightning strike to stun enemies",
    mode_2="Heals the lowest HP Guardian"
)
entry3 = Guardian(
    name="Duncan",
    about="A hulking figure clad in formidable armor, is the stoic guardian of the time-traveling vehicle. With his colossal axe, he cleaves through the fabric of adversaries and stands resolute against any threat. His unwavering determination to protect the artifact is matched only by the weight of his colossal armor, a living testament to his dedication.",
    g_class="Tank",
    attack_type="Melee",
    mode_1="Uses his axe to attack with knockback",
    mode_2="Can no longer move but takes greatly reduced damage and knockback"
)
entry4 = Guardian(
    name="Alex",
    about="The battle mage of arcane lineage, wields a magic sword with the power to manipulate time itself. Swift and deadly, his blade slashes through foes, and with a gesture, he launches projectiles that distort the temporal fabric. Alex stands as the arcane anchor for the group, his every strike resonating with the echoes of past and future, guarding the time-traveling vehicle with his mystical prowess.",
    g_class="Battlemage",
    attack_type="Ranged",
    mode_1="Slashes his sword shooting a magic projectile",
    mode_2="Heals all allies for a small amount"
)
entry5 = Guardian(
    name="Lanxe",
    about="The enigmatic samurai, moves like a phantom on the battlefield. His dual blades are an extension of her very being, and his attacks are a dance of deadly precision. Trained in the art of speed, he guards the time-traveling vehicle with a diligence born of discipline, his keen senses attuned to any temporal disturbances.",
    g_class="Samurai",
    attack_type="Melee",
    mode_1="Has a fast attack speed to deal lots of damage",
    mode_2="Has a slower attack speed but deals more damage and takes less"
)
entry6 = Guardian(
    name="Stephanie",
    about="The huntress with an otherworldly grace, is the mistress of the thrown spear. Her aim is as deadly as her resolve, as she prowls the perimeters safeguarding the temporal vehicle. Her keen eyes pierce through the veil of time, detecting disturbances before they manifest, and her throwing spear strikes true against those who dare to breach the sanctity of the artifact.",
    g_class="Huntress",
    attack_type="Melee/Ranged",
    mode_1="Throws spears with a fast attack speed to deal damage",
    mode_2="Throws spears with a slower attack speed with huge knockback"
)
entry7 = Guardian(
    name="James",
    about="A majestic fire worm, slithers through the fantasy landscape. Born of the very essence of flame, James is a formidable guardian capable of raining fireballs upon intruders. The ability to self-implode as a last resort makes James a living inferno, ensuring that those who threaten the time-traveling vehicle face the wrath of elemental fury.",
    g_class="Fire Worm",
    attack_type="Ranged",
    mode_1="Shoots fireballs for AOE damage",
    mode_2="Flings himself at the enemy and explodes knocking himself out"
)

entry8 = Score(value=3000, user_id=1)

db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8])

db.session.commit()
