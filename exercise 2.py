num = int(input())
maximum = num % 10
while num > 1:
    num //= 10
    if num % 10 > maximum:
        maximum = num % 10
print(maximum)
