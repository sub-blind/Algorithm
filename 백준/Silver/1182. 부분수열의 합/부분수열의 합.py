n, s = map(int,input().split())
lst = list(map(int,input().split()))

cnt = 0

def dfs(num,sum):
	global cnt
	if num >= n:
		return
	sum += lst[num]
	if sum == s:
		cnt += 1

	dfs(num+1,sum)
	dfs(num+1,sum-lst[num])

dfs(0,0)
print(cnt)