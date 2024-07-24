N = int(input())
arr = []
dp = [0,1,2,4]
for i in range(N):
    arr.append(int(input()))
for i in range(4, max(arr)+1):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3]) 

for j in arr:
    print(dp[j])