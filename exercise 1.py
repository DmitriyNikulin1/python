""" Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений"""


def culc():
    operator = input('Введите оператор: ')
    if operator == '0':
        return

    elif operator == '+':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        print(num1 + num2)
        return culc()

    elif operator == '-':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        print(num1 - num2)
        return culc()

    elif operator == '*':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        print(num1 * num2)
        return culc()

    elif operator == '/':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        print(num1 / num2)
        return culc()


culc()
