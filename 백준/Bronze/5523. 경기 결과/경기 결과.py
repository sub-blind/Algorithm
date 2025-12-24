import sys
input = sys.stdin.readline

n = int(input())
t1, t2 = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b: t1 += 1
    elif a < b: t2 += 1
print(t1, t2)