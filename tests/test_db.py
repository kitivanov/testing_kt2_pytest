import sqlite3
import pytest


@pytest.fixture
def db_connection():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()
    yield conn
    conn.close()


def test_insert_user(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    db_connection.commit()

    cursor.execute("SELECT name FROM users WHERE id=1")
    row = cursor.fetchone()

    assert row[0] == "Alice"


def test_empty_table(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    assert rows == []
