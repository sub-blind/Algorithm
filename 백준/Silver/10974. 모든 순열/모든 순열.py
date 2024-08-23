n = int(input())

def dfs(path, visited):
    if len(path) == n:
        print(*path)
        return
    
    for i in range(1, n + 1):
        if not visited & (1 << i):
            dfs(path + [i], visited | (1 << i))

dfs([], 0)
