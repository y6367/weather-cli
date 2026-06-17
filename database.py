import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS weather(date, name, temp, feels_like, humidity, wind, description)')

def insert_weather(date, name, temp, feels_like, humidity, wind, description):
    cursor.execute('CREATE TABLE IF NOT EXISTS weather(date, name, temp, feels_like, humidity, wind, description)')
    cursor.execute(
        "INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?)",
        (date, name, temp, feels_like, humidity, wind, description)
    )
    connection.commit()

# cursor.execute("INSERT INTO weather VALUES ('June 17 2026', 'London', 62.74, 62.67, 84, 7, 'Overcast clouds')")
# cursor.execute('SELECT * FROM weather')

# cursor.execute("DELETE FROM weather WHERE name = 'London'")
# connection.commit()

# result = cursor.fetchone()