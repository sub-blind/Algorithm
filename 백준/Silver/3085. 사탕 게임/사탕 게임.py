import sys
input = sys.stdin.readline

def check(lst):
    max_count = 1
    for i in range(len(lst)):
        row_count = col_count = 1
        for j in range(1, len(lst)):
            # 가로 연속 카운트
            if lst[i][j] == lst[i][j-1]:
                row_count += 1
            else:
                max_count = max(max_count, row_count)
                row_count = 1

            # 세로 연속 카운트
            if lst[j][i] == lst[j-1][i]:
                col_count += 1
            else:
                max_count = max(max_count, col_count)
                col_count = 1

        max_count = max(max_count, row_count, col_count)

    return max_count

n = int(input())
board = [list(input().strip()) for _ in range(n)]
max_result = 0

for i in range(n):
    for j in range(n):
        # 가로로 교환
        if j + 1 < n:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            max_result = max(max_result, check(board))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        # 세로로 교환
        if i + 1 < n:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            max_result = max(max_result, check(board))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(max_result)
