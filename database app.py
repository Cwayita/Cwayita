import sqlite3

connection = sqlite3.connect("Tenants.db")

cur = connection.cursor()

db = cur.execute(
    '''SELECT * FROM Tenants''').fetchall()

print(db)