import sys 
a = int(sys.stdin.readline().strip())
aa = list(map(int, sys.stdin.readline().strip().split()))
b = int(sys.stdin.readline().strip())
bb = list(map(int, sys.stdin.readline().strip().split()))
dic = {}
aa.sort()

for i in aa:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in bb:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print('0', end =' ')
# 배열로 하면 너무 더러워짐