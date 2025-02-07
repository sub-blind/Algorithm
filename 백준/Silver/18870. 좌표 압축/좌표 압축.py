import sys

N = int(sys.stdin.readline().strip())
X = list(map(int, sys.stdin.readline().strip().split()))

dic = {}
for idx, v in enumerate(sorted(set(X))):
    dic[v] = idx

for x in X:
    print(dic[x], end=" ")
