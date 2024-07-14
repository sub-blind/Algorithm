N = int(input())
board = [list(map(int, input().split())) for _ in range(N)] #9*9 2차원 배열

def dfs(x, y, N):
    count = [0, 0, 0]
    num = board[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if board[i][j] != num:
                for k in range(3): # 3*3 재귀 시작
                    for l in range(3):
                        sub_count = dfs(x + k * N // 3, y + l * N // 3, N // 3)
                        count[0] += sub_count[0]
                        count[1] += sub_count[1]
                        count[2] += sub_count[2]
                return count

    if num == -1:
        count[0] = 1
    elif num == 0:
        count[1] = 1
    else:
        count[2] = 1

    return count
result = dfs(0, 0, N)
print(f"{result[0]}\n{result[1]}\n{result[2]}")
