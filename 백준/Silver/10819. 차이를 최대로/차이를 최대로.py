from itertools import permutations
a = int(input())
b = list(map(int, input().split()))

res = 0
for i in permutations(b):
    temp = 0
    for j in range(1, a):
        temp += abs(i[j-1] - i[j] )
    if temp > res:
        res = temp
        
print(res)
