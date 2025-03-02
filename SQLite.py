import sqlite3

# Подключение к базе данных (если базы нет, она будет создана)
conn = sqlite3.connect('example.db')

# Создание курсора
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Вставка данных
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Сохранение изменений
conn.commit()

# Чтение данных
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Закрытие соединения
conn.close()