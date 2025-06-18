num = int(input())
while num > 0 :
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
    num -= 1