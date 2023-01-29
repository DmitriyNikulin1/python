start = float(input())
finish = float(input())
day = 1
if start > finish or start == finish:
    print(f'на {day}-й день спортсмен достиг результата — не менее {finish} км')
while start < finish:
    start = start + start / 10
    day += 1
print(f'на {day}-й день спортсмен достиг результата — не менее {finish} км')
