a = int(input())
 
for i in range(a):
    b = int(input())
    c = int(input())
    lst = [j for j in range(1, c+1)]
    
    for k in range(1, b+1):
        for l in range(1, c):
            lst[l] += lst[l-1]
    print(lst[c-1])