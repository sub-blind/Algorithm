n = int(input())
for _ in range(n):
    a  = int(input())
    max = 0
    name = ""
    for _ in range(a):
        num, player = input().split()
        num = int(num)
        if(num > max):
            max = num
            name = player
    print(name)