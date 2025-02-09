import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = set()
for _ in range(N):
    word = input().strip()
    S.add(word)

count = 0
for _ in range(M):
    check_word = input().strip()
    if check_word in S:
        count += 1

print(count)
