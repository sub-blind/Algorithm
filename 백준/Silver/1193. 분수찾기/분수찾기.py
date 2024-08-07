n = int(input())
ind = 1

while n > ind:
    n -= ind
    ind += 1
if ind % 2 == 0:
    a = n
    b = ind - n + 1
elif ind % 2 == 1:
    a = ind - n + 1
    b = n

print(f'{a}/{b}')