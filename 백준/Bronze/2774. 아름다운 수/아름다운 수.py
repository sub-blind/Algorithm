t = int(input()) 

for _ in range(t):
    a = input()   
    used = []     
    count = 0     

    for ch in a:       
        if ch not in used:  
            used.append(ch)
            count += 1

    print(count)
