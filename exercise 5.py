"""Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число."""


from random import randint


def func(num, c=0):
    if c == 10:
        return num

    ans = int(input())

    if ans == num:
        return 'Ты отгадал'

    elif num < ans:
        c += 1
        print('Слишком больше число')
        func(num, c)
    else:
        c += 1
        print('Слишком маленькое число')
        func(num, c)


num1 = randint(0, 100)
print(func(num1))
