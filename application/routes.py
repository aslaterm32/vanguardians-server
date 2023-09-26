from application import app, db
from werkzeug import exceptions
from flask import request, jsonify
from application.models import User, Guardian, Score
from .controllers import show, index


def format_user(user):
    return {
        "user_id": user.user_id,
        "username": user.username,
        "email": user.email,
        "password": user.password,
    }


def format_score(score):
    print(score.username)
    return {
        "score_id": score.score_id,
        "value": score.value,
        "user_id": score.user_id,
        "username": score.username,
    }


def format_guardian(guardian):
    return {
        "g_id": guardian.g_id,
        "name": guardian.name,
        "about": guardian.about,
        "g_class": guardian.g_class,
        "attack_type": guardian.attack_type,
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


@app.route("/users", methods=["GET", "POST"])
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
    elif request.method == "POST":
        try:
            data = request.json
            user = User(data["username"], data["email"], data["password"])
            db.session.add(user)
            db.session.commit()
            return "User successfully created", 201
        except:
            return "Failed to create user", 400


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
            scores = Score.query.join(User).add_columns(
                Score.score_id, Score.value, Score.user_id, User.username
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


@app.route("/guardians", methods=["POST", "GET"])
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
