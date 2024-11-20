from collections import deque

d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def bfs():
    q = deque()
    # 시작점: 모든 상어 위치를 큐에 추가
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                q.append((y, x))
                visited[y][x] = 0

    max_distance = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if 0 <= Y < n and 0 <= X < m and visited[Y][X] == -1:
                visited[Y][X] = visited[y][x] + 1
                max_distance = max(max_distance, visited[Y][X])
                q.append((Y, X))

    return max_distance

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]  # 초기 방문 배열

print(bfs())
