import sys
input = sys.stdin.readline

words = set()
for _ in range(2):
    words.update(input().split())

words = sorted(words)

for a in words:
    for b in words:
        print(a, b)
