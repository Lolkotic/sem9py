# 4) Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора *.
# Второй — более сложная реализация без оператора *, предусматривающая использование цикла.


def my_func(x, y):
    try:
        return x ** y
    except: y >= 0
    print("Wrong numbers")

print(my_func(x=float(input("Введите целое положительное число: ")),
            y=int(input("Введите целое отрицательное число: "))))