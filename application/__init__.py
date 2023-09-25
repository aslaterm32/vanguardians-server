from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://fjdjlwpd:oz_r0i-S4TMM3VsmDjQSGvyMTGUc9aUo@tai.db.elephantsql.com/fjdjlwpd"
db = SQLAlchemy(app)

from application import routes
