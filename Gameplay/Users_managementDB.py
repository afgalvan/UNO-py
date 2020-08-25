import sqlite3
from subprocess import run

conn = sqlite3.connect("Players.sqlite")
cur = conn.cursor()

def reset_data():
    cur.executescript("""
    DROP TABLE IF EXISTS Users;

    CREATE TABLE Users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        username TEXT UNIQUE,
        matches INTEGER NOT NULL,
        wins INTEGER NOT NULL,
        loses INTEGER NOT NULL,
        winrate REAL NOT NULL
    );
    """)

def validate_user(username):
    cur.execute("""SELECT username FROM Users
    WHERE LOWER(username) = ?""", (username.lower(), ))
    try:
        DB_username = cur.fetchone()[0]
        return True
    except:
        return False


def insert_to_DB(username):
    cur.execute("""INSERT INTO Users(username, matches, wins, loses, winrate)
    VALUES(?, ?, ?, ?, ?)""", (username, 0, 0, 0, 0))


def create_user():
    exists = True
    while exists:
        username = input("Enter a user name: ")
        exists = validate_user(username)
        if exists: print("\nUsername already taken.\n")

    insert_to_DB(username)
    conn.commit()
    return username


def load_user():
    exists = False
    while not exists:
        username = input("Enter your username: ")
        exists = validate_user(username)
        if not exists: print("\nUsername doesn't exists.\n")
    
    conn.commit()
    
    return username


def save_stats(username, matches, wins, loses):
    cur.execute("""SELECT id FROM Users
    WHERE LOWER(username) = ?""", (username.lower(), ))
    user_id = cur.fetchone()[0]

    cur.execute("""SELECT matches, wins, loses FROM Users
    WHERE id = ? """, (user_id, ))
    user_stats = cur.fetchone()

    matches += user_stats[0]
    wins += user_stats[1]
    loses += user_stats[2]

    cur.execute("""UPDATE Users SET matches = ?, wins = ?,
    loses = ?, winrate = ? WHERE id = ?""",
    (matches, wins, loses, (wins/matches) * 100, user_id))
    
    conn.commit()