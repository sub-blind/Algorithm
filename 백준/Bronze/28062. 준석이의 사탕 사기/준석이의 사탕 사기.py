N = int(input())
a = list(map(int, input().split()))
a.sort()
total = sum(a)

if N == 1:
    if a[0] % 2 == 0:
        print(a[0])
    else:
        print(0)
        
else:
    if total % 2 == 0:
        print(total)
    else:
        for num in a:
            if num % 2 != 0:
                print(total - num)
                break
