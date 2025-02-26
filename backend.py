from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create database and table if not exists
def init_db():
    conn = sqlite3.connect("logins.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username_or_email = data.get("usernameOrEmail")
    password = data.get("password")

    if not username_or_email or not password:
        return jsonify({"message": "Username and password required!"}), 400

    conn = sqlite3.connect("logins.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username_or_email,))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "User already exists!"}), 400

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username_or_email, password))
    conn.commit()
    conn.close()

    return jsonify({"message": "Login successful!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
