from collections import deque

def input_graph():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    return N, V, graph

def bfs(V, graph, visited):
    q = deque([V])
    visited[V] = True
    while q:
        node = q.popleft()
        print(node, end=" ")
        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True

def dfs(V, graph, visited):
    visited[V] = True
    print(V, end=" ")
    for neighbor in sorted(graph[V]):
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)

def main():
    N, V, graph = input_graph()
    
    visited_dfs = [False] * (N + 1)
    visited_bfs = [False] * (N + 1)
    
    dfs(V, graph, visited_dfs)
    print()
    bfs(V, graph, visited_bfs)

if __name__ == "__main__":
    main()
