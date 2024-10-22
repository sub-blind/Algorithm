import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0

for i in range(N):
    A[i] -= B
    result += 1

    if A[i] > 0:
        if A[i] % C == 0:
            result += A[i]//C
        else:
            result += A[i]//C + 1

print(result)