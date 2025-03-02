# Запись в файл
with open("example.txt", "w") as file:
    file.write("Hello, file!")

# Чтение из файла
with open("example.txt", "r") as file:
    content = file.read()
    print(content)