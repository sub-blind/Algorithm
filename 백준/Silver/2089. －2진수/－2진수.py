n = int(input())
result = ''

if n == 0:
    print('0')
else:
    while n != 0:
        remainder = n % -2
        n = n // -2
        
        if remainder < 0:
            remainder += 2
            n += 1
        
        result = str(remainder) + result
    
    print(result)
