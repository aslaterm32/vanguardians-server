from application import db, app

app.app_context().push()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    scores = db.relationship("Score", backref="user")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"user_id: {self.user_id}\nusername: {self.username}\npassword: {self.password}"


class Score(db.Model):
    score_id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

    def __init__(self, value, user_id):
        self.value = value
        self.user_id = user_id

    def __repr__(self):
        return (
            f"score_id: {self.score_id}\nvalue: {self.value}\nuser_id: {self.user_id}"
        )


class Guardian(db.Model):
    g_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    about = db.Column(db.String(200), nullable=False)
    g_class = db.Column(db.String(20), nullable=False)
    attack_type = db.Column(db.String(20), nullable=False)
    sprite = db.Column(db.String(300), nullable=True)

    def __init__(self, name, about, g_class, attack_type, sprite):
        self.name = name
        self.about = about
        self.g_class = g_class
        self.attack_type = attack_type
        self.sprite = sprite

    def __repr__(self):
        return f"g_id: {self.g_id}, name: {self.name}"

    @property
    def json(self):
        return {
            "g_id": self.g_id,
            "name": self.name,
            "about": self.about,
            "g_class": self.g_class,
            "attack_type": self.attack_type,
            "sprite": self.sprite,
        }
