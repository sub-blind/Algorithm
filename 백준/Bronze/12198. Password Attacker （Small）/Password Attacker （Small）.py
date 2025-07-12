MOD = 10**9 + 7

from math import comb

T = int(input())

fact = [1] * 8
for i in range(1, 8):
    fact[i] = fact[i - 1] * i

dp = [[0] * 8 for _ in range(8)]
for m in range(1, 8):
    for n in range(m, 8):
        total = m ** n
        for k in range(1, m):
            total -= comb(m, k) * dp[k][n]
        dp[m][n] = total

for t in range(1, T + 1):
    M, N = map(int, input().split())
    print(f"Case #{t}: {dp[M][N] % MOD}")
