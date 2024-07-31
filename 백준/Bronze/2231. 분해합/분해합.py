import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    summer = i + sum(map(int, str(i)))
    if summer == n:
        print(i)
        break
else:
    print(0)