import sys

input = sys.stdin.readline

n = int(input())
sg_cards = set(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

result = []

for num in targets:
    if num in sg_cards:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))
