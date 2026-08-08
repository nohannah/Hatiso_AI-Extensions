import sqlite3

DB_NAME = "predictions.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        comment TEXT,

        prediction TEXT,

        confidence REAL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()


def init_db():
    create_table()
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        comment TEXT,

        prediction TEXT,

        confidence REAL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()

def save_prediction(comment, prediction, confidence):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO predictions

        (comment,prediction,confidence)

        VALUES(?,?,?)

    """,(comment,prediction,confidence))

    conn.commit()

    conn.close()

def get_predictions():

    conn=sqlite3.connect(DB_NAME)

    cursor=conn.cursor()

    cursor.execute("""

        SELECT *

        FROM predictions

        ORDER BY id DESC

    """)

    rows=cursor.fetchall()

    conn.close()

    return rows


def get_history():
    return get_predictions()