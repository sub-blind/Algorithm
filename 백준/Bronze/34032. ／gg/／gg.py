import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

if S.count('O') >= (N + 1) // 2:
    print("Yes")
else:
    print("No")
