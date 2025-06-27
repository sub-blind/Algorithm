N = int(input())

for _ in range(N):
    lis = list(map(int, input().split()))
    lis.sort()
    if lis[3] - lis[1] >= 4:
        print("KIN")
    else:
        print(sum(lis[1:4]))