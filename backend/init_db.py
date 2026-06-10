import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS options (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL,
    answers TEXT NOT NULL
)
""")

standard = [
    ("Вік", ["до 25", "25-45", "45+"]),
    ("Стать", ["Чоловік", "Жінка"]),
    ("Чи подобається сервіс?", ["Так", "Ні"])
]

for text, opts in standard:
    cursor.execute("SELECT id FROM questions WHERE text=?", (text,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO questions (text) VALUES (?)", (text,))
        qid = cursor.lastrowid
        for o in opts:
            cursor.execute("INSERT INTO options (question_id, text) VALUES (?, ?)", (qid, o))

conn.commit()
conn.close()
print("Стандартні питання створено")
