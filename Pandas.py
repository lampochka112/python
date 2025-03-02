# Пример для работы с данными в таблицах (CSV)
import pandas as pd

# Создание DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 27, 22]}
df = pd.DataFrame(data)

# Сохранение DataFrame в CSV
df.to_csv('people.csv', index=False)

# Чтение из CSV
df = pd.read_csv('people.csv')
print(df)