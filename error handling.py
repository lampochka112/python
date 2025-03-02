try:
    x = 10 / 0  # Деление на ноль
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")