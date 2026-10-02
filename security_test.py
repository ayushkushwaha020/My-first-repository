import pickle
import sqlite3

API_TOKEN = "test-secret-value"

def load_user(raw):
    return pickle.loads(raw)

def get_user(name):
    db = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return db.execute(query).fetchone()
