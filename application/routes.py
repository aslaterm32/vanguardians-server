from application import app, db
from werkzeug import exceptions
from flask import request, jsonify
from application.models import User


def format_user(user):
    return {
        "user_id": user.user_id,
        "username": user.username,
        "email": user.email,
        "password": user.password,
    }


@app.route("/")
def home():
    return "<h1>ROUTES</h1><span>GET /users</span>"


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


# @app.route("/users/<id>", methods=["PATCH", "DELETE"])
# def user_id_route(id):
#     if request.method == "PATCH":

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
  return jsonify({"error": f"ERR: {err}"}), 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
  return jsonify({"error": f"ERR: {err}"}), 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
  return jsonify({"error": f"ERR: {err}"}), 400
