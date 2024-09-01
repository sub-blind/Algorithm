n = int(input().strip())

sums = set()

for i in range(n + 1):
    for j in range(n + 1 - i):
        for k in range(n + 1 - i - j):
            total = i * 1 + j * 5 + k * 10 + (n - i - j - k) * 50
            sums.add(total)

print(len(sums))
