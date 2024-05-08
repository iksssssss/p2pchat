import sqlite3


connection = sqlite3.connect('db.db')

crsr = connection.cursor()
sql_command = "SELECT * FROM messages"
crsr.execute(sql_command)
connection.commit()

data = crsr.fetchall()


for a in data:
    print(a)