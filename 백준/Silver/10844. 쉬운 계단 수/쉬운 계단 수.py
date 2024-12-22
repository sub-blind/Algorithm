N = int(input())
MOD = 1000000000

prev_dp = [0] * 10
current_dp = [0] * 10

for i in range(1, 10):
    prev_dp[i] = 1

for _ in range(2, N + 1):
    current_dp[0] = prev_dp[1]
    for j in range(1, 9):
        current_dp[j] = (prev_dp[j - 1] + prev_dp[j + 1]) % MOD
    current_dp[9] = prev_dp[8]

    prev_dp, current_dp = current_dp, [0] * 10

print(sum(prev_dp) % MOD)
