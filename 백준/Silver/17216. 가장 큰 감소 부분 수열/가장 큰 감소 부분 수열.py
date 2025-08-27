import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = arr[:]
for i in range(N):
    for j in range(i):
        if arr[j] > arr[i]:
            if dp[j] + arr[i] > dp[i]:
                dp[i] = dp[j] + arr[i]

print(max(dp))
