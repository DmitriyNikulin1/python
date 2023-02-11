"""Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа."""


def numb(num, even=0, odd=0):
    if not num:
        return even, odd
    if num % 10 % 2 == 1:
        odd += 1
    else:
        even += 1
    return numb(num//10, even, odd)


n = int(input('Введите число: '))
print(numb(n))
