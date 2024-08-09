import sys
dp = [0] * 1000001
Sum = [0] * 1000001
for i in range(1, 1000001):
    j = 1
    while i * j < 1000001:
        dp[i * j] += i
        j += 1
    Sum[i] = Sum[i - 1] + dp[i]

n = int(input())
for _ in range(n):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(Sum[a]) + "\n")
