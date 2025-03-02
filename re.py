import re

text = "My phone number is 123-456-7890"

# Поиск телефонного номера с помощью регулярного выражения
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print(f"Found phone number: {match.group()}") 