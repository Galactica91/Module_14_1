import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")
#cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)", ("user", "ex@gmail.com", "20", "1000"))
#for i in range(1, 11):
#    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)", (f"user{i}", f"ex{i}@gmail.com", i*10, 1000))

cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1000")
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
rows = cursor.fetchall()
for row in rows:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

connection.commit()
connection.close()
