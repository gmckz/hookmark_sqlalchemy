import pytest, sys, random, py, pytest, os
from lib.database_connection import DatabaseConnection
from server import app

@pytest.fixture
def db_connection():
    os.environ['APP_ENV'] = 'test'  # Set APP_ENV explicitly

    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    return conn

@pytest.fixture
def web_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client