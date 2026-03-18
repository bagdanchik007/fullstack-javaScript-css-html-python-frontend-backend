from flask import Flask, request, jsonify, render_template
import sqlite3
import bcrypt

app = Flask(__name__)

# -------------------------
# Datenbank erstellen
# -------------------------
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password BLOB
    )
    """)

    conn.commit()
    conn.close()

init_db()

# -------------------------
# Startseite (HTML laden)
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------------
# REGISTER
# -------------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    password = data["password"]

    # Passwort hashen
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed_password)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "User registered successfully"})


# -------------------------
# LOGIN
# -------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        stored_password = user[0]

        if bcrypt.checkpw(password.encode("utf-8"), stored_password):
            return jsonify({"message": "Login successful"})
        else:
            return jsonify({"message": "Wrong password"}), 401
    else:
        return jsonify({"message": "User not found"}), 404


# -------------------------
# Server starten
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)