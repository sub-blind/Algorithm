import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for n in range(N):
    key, value = input().split()
    dic[key] = value

for m in range(M):
    key = input().strip()
    print(dic[key])