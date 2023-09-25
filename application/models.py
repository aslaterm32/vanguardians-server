from application import db, app

app.app_context().push()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"user_id: {self.user_id}\nusername: {self.username}\nemail: {self.email}\npassword: {self.password}"

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    c_class = db.Column(db.String(20), nullable=False)
    attack_type = db.Column(db.String(20), nullable=False)

    def __init__(self, name, c_class, attack_type):
        self.name = name
        self.c_class = c_class
        self.attack_type = attack_type

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, c_class: {self.c_class}, attack_type: {self.attack_type}"

    @property
    def json(self):
        return{"id": self.id, "name": self.name, "c_class": self.c_class, "attack_type": self.attack_type}
