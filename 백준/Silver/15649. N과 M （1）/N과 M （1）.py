n, m = list(map(int, input().split()))
s = []
temp = [False] * (n + 1)
def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n + 1):
        if not temp[i]:
            s.append(i)
            temp[i] = True
            dfs()
            s.pop()
            temp[i] = False
dfs()