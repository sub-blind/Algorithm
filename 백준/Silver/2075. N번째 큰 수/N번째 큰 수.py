import sys
import heapq

read = sys.stdin.readline
size = int(read())

numbers = []

for _ in range(size):
    row = map(int, read().split())
    for value in row:
        if len(numbers) < size:
            heapq.heappush(numbers, value)
        elif value > numbers[0]:
            heapq.heapreplace(numbers, value)

print(numbers[0])
