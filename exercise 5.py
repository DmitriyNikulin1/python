my_str = input()
my_list = my_str.split(' ')
for i in range(1, len(my_list)+1):
    if len(my_list[i-1]) < 10:
        print(i, '. ', my_list[i-1], sep='')
    else:
        print(i, '. ', my_list[i-1][0:10], sep='')
