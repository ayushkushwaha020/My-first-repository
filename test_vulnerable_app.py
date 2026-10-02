import os
import sqlite3
import subprocess

API_KEY = "sk-test-hardcoded-secret-123456"

def find_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def run_backup(folder):
    command = "tar -czf backup.tar.gz " + folder
    return subprocess.run(command, shell=True, capture_output=True, text=True)

def check_users(users, target):
    for user in users:
        for other in users:
            if user == target and other == target:
                return True
    return False

def login(username, password):
    if password == "admin123":
        return {"user": username, "admin": True}
    return None

if __name__ == "__main__":
    print(find_user(input("Username: ")))