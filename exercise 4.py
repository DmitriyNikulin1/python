"""Задание 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры."""


def calculation(n, s, c):
    s = s + c
    c = c / -2
    n -= 1
    if n < 1:
        return s
    return calculation(n, s, c)


num = int(input('Введите число: '))
summa = 0
count = 1
print(calculation(num, summa, count))
