import sys
input = sys.stdin.readline

n = int(input())
weights = [int(input()) for _ in range(n)]

total = sum(weights)
half = n // 2

dp = [0] * (half + 1)
dp[0] = 1

for w in weights:
    for i in range(half, 0, -1):
        dp[i] |= dp[i-1] << w

min_gap = float('inf')
best = 0

bitset = dp[half]

for s in range(total + 1):
    if (bitset >> s) & 1:
        gap = abs(total - 2*s)
        if gap < min_gap:
            min_gap = gap
            best = s

a = best
b = total - best

if a > b:
    a, b = b, a

print(a, b)