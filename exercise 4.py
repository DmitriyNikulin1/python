nums = int(input('Введите количество чисел которые хоитите добавить: '))
el = 0
my_list = []
for i in range(nums):
    num = int(input())
    my_list.append(num)
for i in range(int(len(my_list)/2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)
