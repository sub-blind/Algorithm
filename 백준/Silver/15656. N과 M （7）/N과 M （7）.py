n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result=[]
def dfs(num):
    if len(result)==m:
        print(*result)
        return
    for i in range(num, len(arr)):
        result.append(arr[i])
        dfs(0)
        result.pop()
dfs(0)