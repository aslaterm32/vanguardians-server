from .models import User, Guardian
from werkzeug import exceptions
from flask import jsonify, request
from . import db
import json

def index():
  try:
    guardians = Guardian.query.all()
    data = [c.json for c in guardians]
    return jsonify({"guardians": data})
  except:
    raise exceptions.InternalServerError("We are working on it")
  
def show(id):
  try:
    guardian = Guardian.query.filter_by(g_id=id).first()
    return jsonify({"data": guardian.json}), 200
  except:
    raise exceptions.NotFound("")
