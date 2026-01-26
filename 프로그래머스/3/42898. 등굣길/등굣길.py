def dfs(x, y, dp):
    n = len(dp)
    m = len(dp[0])

    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            if i == 0 and j == 0:
                continue

            left = 0
            up = 0

            if j - 1 >= 0 and dp[i][j - 1] != -1:
                left = dp[i][j - 1]
            if i - 1 >= 0 and dp[i - 1][j] != -1:
                up = dp[i - 1][j]

            dp[i][j] = left + up

    return dp[y][x]


def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for p in puddles:
        x, y = p
        dp[y - 1][x - 1] = -1

    dp[0][0] = 1
    ans = dfs(m - 1, n - 1, dp)
    return ans % 1000000007
