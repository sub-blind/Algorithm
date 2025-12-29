t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(str(list(range(n, m + 1))).count('0'))
