import sys
n = int(sys.stdin.readline().strip())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
b = [1] * n
for i in range(n):
    for j in range(n):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            b[i] += 1
print(" ".join(map(str, b)))
