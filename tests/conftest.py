import pytest
from flask_sqlalchemy import SQLAlchemy
import application.routes


@pytest.fixture()
def app():
    app = application.routes.app
    db = application.routes.db

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    with app.test_client() as client:
        yield client
