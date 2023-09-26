from application import app, db
from werkzeug import exceptions
from flask import request, jsonify
from application.models import User, Guardian
from .controllers import show, index


def format_user(user):
    return {
        "user_id": user.user_id,
        "username": user.username,
        "email": user.email,
        "password": user.password,
    }

def format_guardian(guardian):
    return {
        "g_id" : guardian.g_id,
        "name" : guardian.name,
        "about" : guardian.about,
        "g_class": guardian.g_class,
        "attack_type": guardian.attack_type
    }

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome",
        "description": "Vanguardians API",
        "endpoints": [
            "GET /",
            "GET /users",
            "GET /guardians",
            "GET /guardians/:id"
        ]
    }, 200)


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
            print(data)
            user = User(data["username"], data["email"], data["password"])
            db.session.add(user)
            db.session.commit()
            return "User successfully created", 201
        except:
            return "Failed to create user", 500


# @app.route("/users/<int:id>", methods=["PATCH", "DELETE"])
# def user_id_route(id):
#     if request.method == "PATCH":


@app.route("/guardians", methods=["POST", "GET"])
def handle_guardians():
    if request.method == "GET": return index()

@app.route("/guardians/<int:id>", methods=["GET"])
def handle_guardian(id):
    if request.method == "GET": return show(id)


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
  return jsonify({"error": f"ERR: {err}"}), 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
  return jsonify({"error": f"ERR: {err}"}), 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
  return jsonify({"error": f"ERR: {err}"}), 400
