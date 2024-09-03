n, m = map(int, input().split())
answer = list(map(int, input().split()))
result = []
answer.sort()

def dfs():
    if len(result) == m:
        print(*result)
        return
    for i in answer:
        if i in result:
            continue
        if len(result) != 0 and result[-1] >= i:
            continue
        result.append(i)
        dfs()
        result.pop()

dfs()