import sys
input = sys.stdin.readline

MOD = 1000000009

n = int(input().strip())

result = 1
for i in range(1, n + 1):
    result = result * (2 * i - 1) % MOD

print(result)
