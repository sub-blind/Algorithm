def solution(n, k):
    a = n*12000
    if n >= 10:
        b= (k-n//10)*2000
    else:
        b = k*2000
        
    answer = a+b
    return answer