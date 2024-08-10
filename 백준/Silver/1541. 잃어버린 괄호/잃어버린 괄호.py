import sys
arr = sys.stdin.readline().strip().split('-')
answer = sum(map(int, arr[0].split('+')))

for i in arr[1:]:
    answer -= sum(map(int, i.split('+')))

print(answer)
