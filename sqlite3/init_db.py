import sqlite3

connection = sqlite3.connect('flask.db')


with open('sql.sql') as f:
    connection.executescript(f.read())

print("finished db")
