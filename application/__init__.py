from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.json_provider_class.sort_keys = False
CORS(
    app  # , resources={r"/users": {"origins": "http://localhost:5173"}}, supports_credentials=True  <-- Uncomment for deployed repo
)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]

db = SQLAlchemy(app)
