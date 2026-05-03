from flask import Flask, render_template, request, jsonify
from password_checker import analyze_password
from datetime import datetime
import os

app = Flask(__name__)

REPORT_FILE = "reports/history.txt"

os.makedirs("reports", exist_ok=True)


def save_report(password, result):
    with open(REPORT_FILE, "a", encoding="utf-8") as file:
        file.write(
            f"[{datetime.now()}] Password: {password} | "
            f"Strength: {result['strength']} | "
            f"Score: {result['score']}% | "
            f"Entropy: {result['entropy']} bits\n"
        )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check_password():
    data = request.get_json()
    password = data.get("password", "")

    result = analyze_password(password)
    save_report(password, result)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)