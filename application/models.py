from application import db, app

app.app_context().push()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    score = db.relationship("Score", backref="user", cascade="all, delete-orphan")
    token = db.relationship("Token", backref="user", cascade="all, delete-orphan")
    stat = db.relationship("Stat", backref="user", cascade="all, delete-orphan")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"user_id: {self.user_id}\nusername: {self.username}\npassword: {self.password}"


class Token(db.Model):
    token_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(100), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def __repr__(self):
        return (
            f"token_id: {self.token_id}\ntoken: {self.token}\nuser_id: {self.user_id}"
        )


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


class Stat(db.Model):
    stat_id = db.Column(db.Integer, primary_key=True)
    hours_played = db.Column(db.Integer, nullable=False)
    metres_gained = db.Column(db.Integer, nullable=False)
    enemies_defeated = db.Column(db.Integer, nullable=False)
    damage_given = db.Column(db.Integer, nullable=False)
    damage_recieved = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

    def __init__(
        self,
        hours_played,
        metres_gained,
        enemies_defeated,
        damage_given,
        damage_recieved,
        user_id,
    ):
        self.hours_played = hours_played
        self.metres_gained = metres_gained
        self.enemies_defeated = enemies_defeated
        self.damage_given = damage_given
        self.damage_recieved = damage_recieved
        self.user_id = user_id

    def __repr__(self):
        return f"hours_played: {self.hours_played}\nenemies_defeated: {self.enemies_defeated}\ndamage_given: {self.damage_recieved}\ndamage_recieved: {self.damage_recieved}"


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
