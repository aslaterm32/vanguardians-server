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

# class Character(db.Model):
#     character_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Integer, nullable=False)
#     character_class = db.Column(db.String(10), nullable=False)
#     character_id = db.Column(db.Integer, nullable=False)
