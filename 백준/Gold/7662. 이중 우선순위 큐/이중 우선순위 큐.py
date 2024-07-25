import sys, heapq
input = sys.stdin.readline
a = int(input())
for _ in range(a):
    b= int(input())
    heapmax = []
    heapmin = []
    visit = [False] * b

    for i in range(b):
        c, d = input().split()
        d = int(d)

        if c == 'I':
            heapq.heappush(heapmin, (d, i))
            heapq.heappush(heapmax, (-d, i))
            visit[i] = True

        elif c == 'D':
            if d == 1:
                while heapmax and not visit[heapmax[0][1]]:
                    heapq.heappop(heapmax)
                if heapmax:
                    d, i = heapq.heappop(heapmax)
                    visit[i] = False
            elif d == -1:
                while heapmin and not visit[heapmin[0][1]]:
                    heapq.heappop(heapmin)
                if heapmin:
                    d, i = heapq.heappop(heapmin)
                    visit[i] = False
                    
    while heapmin and not visit[heapmin[0][1]]:
        heapq.heappop(heapmin)
    while heapmax and not visit[heapmax[0][1]]:
        heapq.heappop(heapmax)

    if heapmax and heapmin:
        print(-heapmax[0][0], heapmin[0][0])
    else:
        print('EMPTY')
