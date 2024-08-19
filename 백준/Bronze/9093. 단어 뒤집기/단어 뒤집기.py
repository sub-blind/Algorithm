import sys

N = int(input())

for _ in range(N):
    words = sys.stdin.readline().rstrip().split()
    print(" ".join(word[::-1] for word in words))
