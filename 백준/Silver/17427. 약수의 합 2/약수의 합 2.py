import sys
input=sys.stdin.readline
result = 0
n = int(input())
for i in range(1, n+1):
    result += (n//i)*i
print(result)