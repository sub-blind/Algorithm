import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

dequeue = deque()
result = []

for _ in range(n):
    command = list(map(int, input().split()))
    
    if command[0] == 1:
        dequeue.appendleft(command[1])
    elif command[0] == 2:
        dequeue.append(command[1])
    elif command[0] == 3:
        result.append(dequeue.popleft() if dequeue else -1)
    elif command[0] == 4:
        result.append(dequeue.pop() if dequeue else -1)
    elif command[0] == 5:
        result.append(len(dequeue))
    elif command[0] == 6:
        result.append(0 if dequeue else 1)
    elif command[0] == 7:
        result.append(dequeue[0] if dequeue else -1)
    elif command[0] == 8:
        result.append(dequeue[-1] if dequeue else -1)

sys.stdout.write("\n".join(map(str, result)) + "\n")
