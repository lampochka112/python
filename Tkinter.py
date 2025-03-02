import tkinter as tk

def on_click():
    label.config(text="Hello, Tkinter!")

# Создание главного окна
root = tk.Tk()

# Создание метки
label = tk.Label(root, text="Press the button")
label.pack()

# Создание кнопки
button = tk.Button(root, text="Click me", command=on_click)
button.pack()

# Запуск главного цикла
root.mainloop() 