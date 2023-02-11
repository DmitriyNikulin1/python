"""Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран"""


def calculation(n1, n2=0):
    n2 = n2 * 10 + n1 % 10
    n1 //= 10
    if n1 == 0:
        return n2
    return calculation(n1, n2)


num = int(input('Введите число: '))
print(calculation(num))
