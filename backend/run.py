from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS options (id INTEGER PRIMARY KEY AUTOINCREMENT, question_id INTEGER NOT NULL, text TEXT NOT NULL, FOREIGN KEY (question_id) REFERENCES questions(id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT NOT NULL, answers TEXT NOT NULL)")
    conn.commit()
    conn.close()

init_db()

@app.route("/get_questions", methods=["GET"])
def get_questions():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, text FROM questions")
    questions = cursor.fetchall()
    result = []
    for q in questions:
        cursor.execute("SELECT text FROM options WHERE question_id=?", (q[0],))
        opts = [row[0] for row in cursor.fetchall()]
        result.append({"id": q[0], "text": q[1], "options": opts})
    conn.close()
    return jsonify(result)

@app.route("/add_questions", methods=["POST"])
def add_questions():
    data = request.get_json()
    questions = data.get("questions", [])
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    for q in questions:
        text = q.get("text", "").strip()
        options = q.get("options", [])
        if text and options:
            cursor.execute("INSERT INTO questions (text) VALUES (?)", (text,))
            qid = cursor.lastrowid
            for opt in options:
                cursor.execute("INSERT INTO options (question_id, text) VALUES (?, ?)", (qid, opt.strip()))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

@app.route("/save_answers", methods=["POST"])
def save_answers():
    data = request.get_json()
    user = data.get("user", "anonymous")
    answers = data.get("answers", {})
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (user, answers) VALUES (?, ?)", (user, json.dumps(answers, ensure_ascii=False)))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

@app.route("/results", methods=["GET"])
def results():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user, answers FROM results")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{"user": r[0], "answers": r[1]} for r in rows])

if __name__ == "__main__":
    app.run(debug=True)
