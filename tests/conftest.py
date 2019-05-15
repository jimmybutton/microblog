# run tests with python -m pytest

import pytest
from app import app, db

@pytest.fixture
def app_fixure():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.create_all()

    yield app, db

    db.session.remove()
    db.drop_all()
