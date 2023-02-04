count = int(input('Введите количество товаров '))
my_dict = []
my_list = []
my_analys = []

for i in range(1, count+1):
    my_dict = dict({'название': input('Введите название товара: '), 'цена': int(input('Введите цену: ')),
                    'количество': int(input('Введите количество: ')), 'eд': input('Введите единицу измерения: ')})
    my_list.append((i, my_dict))
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'),
         'количество': my_dict.get('количество'), 'ед': my_dict.get('ед')}
    )
print(my_list)
print(my_analys)
