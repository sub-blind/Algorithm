import heapq
n = int(input())
card = []
result = 0
for _ in range(n):
    a=int(input())
    heapq.heappush(card, a)
while len(card)>1:
    n1 = heapq.heappop(card)
    n2 = heapq.heappop(card)
    result += n1+n2
    heapq.heappush(card, n1+n2)
print(result)