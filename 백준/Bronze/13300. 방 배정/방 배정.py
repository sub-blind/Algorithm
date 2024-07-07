N , k = map(int, input().split()) 

arr = [[0] * 6 for _ in range(2)]
result = 0
for i in range(N):
    a , b  = map(int, input().split())
    arr[a][b - 1] += 1

for i in arr :
    for j in i:
        if j % k == 0:
            result += j//k
        else:
            result += (j//k) + 1
print(result)