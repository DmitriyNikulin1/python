month = int(input('Введите номер месяца: '))
lst = ['Зима', 'Весна', 'Лето', 'Осень']
dct = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}


if month == 1 or month == 12 or month == 2:
    print(f'Результат через список: {lst[0]}')
    print(f'Результат через словарь: {dct.get(1)}')

elif month == 3 or month == 4 or month == 5:
    print(f'Результат через список: {lst[1]}')
    print(f'Результат через словарь: {dct.get(2)}')

elif month == 6 or month == 7 or month == 8:
    print(f'Результат через список: {lst[2]}')
    print(f'Результат через словарь: {dct.get(3)}')

elif month == 9 or month == 10 or month == 11:
    print(f'Результат через список: {lst[3]}')
    print(f'Результат через словарь: {dct.get(4)}')

else:
    print('Такого месяца не существует')
