n = int(input())
dp =[0] + list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(i):
        dp[i]= min(dp[i], dp[j]+dp[i-j])
print(dp[n])