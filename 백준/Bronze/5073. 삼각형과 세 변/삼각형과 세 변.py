import sys

for i in sys.stdin:
    a, b, c = map(int, i.split())
    
    if a == b == c == 0:
        break
    
    longest = max(a, b, c)
    total = a + b + c
    
    if longest >= total - longest:
        print('Invalid')
        continue
    
    if a == b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')