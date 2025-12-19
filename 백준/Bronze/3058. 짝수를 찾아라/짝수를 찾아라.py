a = int(input())

for _ in range(a):
    b = list(map(int, input().split()))
    even = []
    
    for i in b:
        if i % 2 == 0:
            even.append(i) 
    
    print(sum(even), min(even))