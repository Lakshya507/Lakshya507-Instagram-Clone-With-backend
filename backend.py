from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

EXCEL_FILE = "logins.xlsx"

if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=["Username/Email", "Password"])
    df.to_excel(EXCEL_FILE, index=False)


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username_or_email = data.get("usernameOrEmail", "").strip()
    password = data.get("password", "").strip()

    if not username_or_email or not password:
        return jsonify({"message": "Username and password required!"}), 400

    df = pd.read_excel(EXCEL_FILE)

    user = df[df["Username/Email"] == username_or_email]

    if not user.empty:
        stored_password = user.iloc[0]["Password"]
        if stored_password == password:
            return jsonify({"message": "Login successful!", "redirect": "homepage.html"}), 200
        else:
            return jsonify({"message": "Incorrect password!"}), 400
    else:
        new_entry = pd.DataFrame([[username_or_email, password]], columns=["Username/Email", "Password"])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        return jsonify({"message": "Account created automatically! Logging in...", "redirect": "homepage.html"}), 201


if __name__ == "__main__":
    app.run(debug=True)
