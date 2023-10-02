from application import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug import exceptions
from flask import request, jsonify
from application.models import User, Guardian, Score, Token, Stat
from .controllers import show, index
from flask_uuid import uuid


def format_user(user):
    return {
        "user_id": user.user_id,
        "username": user.username,
        "password": user.password,
    }


def format_score(score):
    formatted_score = {
        "score_id": score.score_id,
        "value": score.value,
        "user_id": score.user_id,
    }

    try:
        formatted_score["username"] = score.username
        return formatted_score
    except AttributeError:
        return formatted_score


def format_stat(stat):
    return {
        "stat_id": stat.stat_id,
        "hours_played": stat.hours_played,
        "metres_gained": stat.metres_gained,
        "enemies_defeated": stat.enemies_defeated,
        "damage_given": stat.damage_given,
        "damaage_recieved": stat.damage_recieved,
        "user_id": stat.user_id,
    }


def format_guardian(guardian):
    return {
        "g_id": guardian.g_id,
        "name": guardian.name,
        "about": guardian.about,
        "g_class": guardian.g_class,
        "attack_type": guardian.attack_type,
        "sprite": guardian.sprite,
    }


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Welcome",
            "description": "Vanguardians API",
            "endpoints": [
                "GET /",
                "GET /users",
                "POST /users" "GET /guardians",
                "GET /guardians/:id",
            ],
        },
        200,
    )


@app.route("/users", methods=["GET"])
def user_route():
    if request.method == "GET":
        try:
            users = User.query.all()
            user_list = []
            for user in users:
                user_list.append(format_user(user))
            return user_list, 200
        except:
            return "Failed to fetch users", 404


@app.route("/auth", methods=["POST"])
def auth_route():
    try:
        token = Token.query.filter_by(token=request.headers["token"]).first()
        user = User.query.filter_by(user_id=token.user_id).first()
        return jsonify(format_user(user)), 200
    except:
        return "Could not authenticate user", 401


@app.route("/login", methods=["POST"])
def login_route():
    try:
        data = request.json
        user = User.query.filter_by(username=data["username"]).first()
        if check_password_hash(user.password, data["password"]):
            token = Token(uuid.uuid4(), user.user_id)
            db.session.add(token)
            db.session.commit()
            return jsonify({"authenticated": "true", "token": token.token})
    except:
        return "Failed to find user", 404


@app.route("/register", methods=["POST"])
def register_route():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")
        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return "User successfully created", 201
    except:
        return "Failed to create user", 400


@app.route("/logout", methods=["DELETE"])
def logout_route():
    try:
        tokens = Token.query.filter_by(token=request.headers["token"]).first()
        tokens = Token.query.filter_by(user_id=tokens.user_id).all()
        if tokens:
            for token in tokens:
                db.session.delete(token)
                db.session.commit()
        return "User logged out, tokens deleted", 202
    except:
        return "Unable to log user out", 500


@app.route("/users/<int:id>", methods=["PATCH", "DELETE"])
def user_id_route(id):
    data = request.json
    user = User.query.get(id)
    if request.method == "PATCH":
        try:
            if data["username"]:
                user.username = data["username"]
            if data["email"]:
                user.email = data["email"]
            if data["password"]:
                user.password = data["password"]
            db.session.commit()
            return jsonify(format_user(user)), 200
        except:
            return "Failed to update user", 404
    if request.method == "DELETE":
        try:
            db.session.delete(user)
            db.session.commit()
            return "Successfully deleted user", 200
        except:
            return "Failed to delete user", 404


@app.route("/scores", methods=["GET", "POST"])
def scores_route():
    if request.method == "GET":
        try:
            scores = (
                Score.query.join(User)
                .add_columns(Score.score_id, Score.value, Score.user_id, User.username)
                .order_by(db.desc(Score.value))
            )
            score_list = []
            for score in scores:
                score_list.append(format_score(score))
            return score_list, 200
        except:
            return "Could not get scores", 500
    elif request.method == "POST":
        data = request.json
        try:
            if User.query.get(data["user_id"]):
                score = Score(data["value"], data["user_id"])
                db.session.add(score)
                db.session.commit()
                return f"Score added", 201
            else:
                raise exceptions.NotFound
        except:
            return "Failed to add score", 404


@app.route("/scores/<int:user_id>", methods=["GET"])
def scores_id_route(user_id):
    try:
        scores = Score.query.filter_by(user_id=user_id).all()
        score_list = []
        for score in scores:
            score_list.append(format_score(score))
        return jsonify(score_list), 200
    except:
        return "Failed to identify user", 404


@app.route("/stats", methods=["POST"])
def stats_route():
    try:
        data = request.json
        stat = Stat.query.filter_by(user_id=data["user_id"]).first()
        if stat:
            stat.hours_played += data["hours_played"]
            stat.metres_gained += data["metres_gained"]
            stat.enemies_defeated += data["enemies_defeated"]
            stat.damage_given += data["damage_given"]
            stat.damage_recieved += data["damage_recieved"]
            db.session.commit()
        else:
            stat = Stat(
                hours_played=data["hours_played"],
                metres_gained=data["metres_gained"],
                enemies_defeated=data["enemies_defeated"],
                damage_given=data["damage_given"],
                damage_recieved=data["damage_recieved"],
                user_id=data["user_id"],
            )
            print(stat)
            db.session.add(stat)
            db.session.commit()
        return jsonify(format_stat(stat)), 201
    except:
        return "Unable to save stats", 400


@app.route("/stats/<int:user_id>", methods=["GET"])
def stats_id_route(user_id):
    try:
        stat = Stat.query.filter_by(user_id=user_id).first()
        return jsonify(format_stat(stat)), 200
    except:
        return "User not found", 404


@app.route("/guardians", methods=["GET"])
def handle_guardians():
    if request.method == "GET":
        return index()


@app.route("/guardians/<int:id>", methods=["GET"])
def handle_guardian(id):
    if request.method == "GET":
        return show(id)


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"ERR: {err}"}), 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"ERR: {err}"}), 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error": f"ERR: {err}"}), 400
