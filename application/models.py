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

class Guardian(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    g_class = db.Column(db.String(20), nullable=False)
    attack_type = db.Column(db.String(20), nullable=False)

    def __init__(self, name, about, g_class, attack_type):
        self.name = name
        self.about = about
        self.g_class = g_class
        self.attack_type = attack_type

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, about: {self.about}, g_class: {self.g_class}, attack_type: {self.attack_type}"

    # @property
    # def json(self):
    #     return{"id": self.id, "name": self.name, "g_class": self.g_class, "attack_type": self.attack_type}
