N, K = map(int, input().split())
arr = []
cnt = 0
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in arr:
    if K >= i:
        cnt += K // i
        K %= i
        if K == 0:
            break
print(cnt)