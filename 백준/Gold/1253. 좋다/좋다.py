import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0

for i in range(n):
    target = arr[i]
    seen = set()
    found = False
    
    for j in range(n):
        if j == i:
            continue
        if (target - arr[j]) in seen:
            cnt += 1
            found = True
            break
        seen.add(arr[j])

print(cnt)
