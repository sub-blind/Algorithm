import sys
input = sys.stdin.readline
N, K = map(int, input().split())
a = 1
for i in range(K):
    a *= N
    N -= 1
b = 1
for i in range(2, K+1):
    b *= i
print(a // b)