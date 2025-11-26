n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(start, visited):
    for nxt in range(n):
        if graph[start][nxt] == 1 and not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, visited)

for i in range(n):
    visited = [False] * n
    dfs(i, visited)

    for v in visited:
        print(1 if v else 0, end=' ')
    print()
