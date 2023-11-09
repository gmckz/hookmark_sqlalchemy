import pytest, sys, random, py, pytest, os
from lib.database_connection import DatabaseConnection
from server import app

@pytest.fixture
def db_connection():
    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    return conn

