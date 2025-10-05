n=int(input())
a = list(map(int,input().split()))
cnt =0
for i in range(3):
    if a[i] <= n:
        cnt += a[i]
    else:
        cnt += n
print(cnt)
