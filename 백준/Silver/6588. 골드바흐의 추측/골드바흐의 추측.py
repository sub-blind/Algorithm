import sys
input = sys.stdin.read
lst = [True] * 1000001
lst[0] = lst[1] = False
m = int(1000001**0.5)
for i in range(2, m + 1):
    if lst[i]:
        for k in range(i * i, 1000001, i):
            lst[k] = False

data = input().split()
for n in map(int, data):
    if n == 0:
        break
    found = False
    for i in range(2, n // 2 + 1):
        if lst[i] and lst[n - i]:
            print(f"{n} = {i} + {n - i}")
            found = True
            break
