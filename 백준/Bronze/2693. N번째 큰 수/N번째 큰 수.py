T = int(input())

for i in range(T) :
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    print(s[2])