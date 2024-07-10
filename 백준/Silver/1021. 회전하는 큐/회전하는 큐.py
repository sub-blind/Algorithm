import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = deque([])

for _ in range(1, n + 1):
    a.append(_)
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    while True:
        if num == a[0]:
            a.popleft()
            break
        else:
            if a.index(num) > len(a) // 2:
                a.appendleft(a.pop())
                cnt += 1
            else:
                a.append(a.popleft())
                cnt += 1

print(cnt)