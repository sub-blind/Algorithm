def solution(name, yearning, photo):
    answer = []
    
    a = dict(zip(name, yearning))
    
    for b in photo:
        
        counter = 0
        
        for c in b:
            counter += a.get(c, 0)
        answer.append(counter)
        
    return answer