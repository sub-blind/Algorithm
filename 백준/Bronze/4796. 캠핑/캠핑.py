i = 0
while True:
    l, p, v = map(int, input().split())
    
    if l == 0 and p == 0 and v == 0:
        break
    
    a = v // p
    b = v % p
    b = min(b, l)
    
    i += 1
    print(f"Case {i}: {a * l + b}")
