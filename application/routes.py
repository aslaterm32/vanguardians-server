from application import app, db
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


@app.route("/users", methods=["GET"])
def user_route():
    if request.method == "GET":
        users = User.query.all()
        user_list = []
        for user in users:
            user_list.append(format_user(user))
        return user_list
