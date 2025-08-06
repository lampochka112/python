#  Факториал числа
# Задание 5.э

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Введите число для вычисления факториала: "))
print(f"Факториал числа {number} равен: {factorial(number)}")
