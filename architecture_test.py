import json
import sqlite3
import requests

def process_order(order):
    db = sqlite3.connect("orders.db")
    db.execute("INSERT INTO orders VALUES (?)", (json.dumps(order),))
    response = requests.post("https://example.com/events", json=order)
    if response.status_code == 200:
        return {"saved": True, "event": response.json()}
    return {"saved": True, "event": None}