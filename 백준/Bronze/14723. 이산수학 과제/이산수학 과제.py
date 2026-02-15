n = int(input())

i = 1
while True:
    total = i * (i + 1) // 2
    if total >= n:
        break
    i += 1

tot = (i - 1) * i // 2
b = n - tot
a = i + 1 - b

print(a, b)
