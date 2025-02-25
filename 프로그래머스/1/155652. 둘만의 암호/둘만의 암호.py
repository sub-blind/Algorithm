def solution(s, skip, index):
    a = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    
    for i in list(skip):
        a = a.replace(i,"")
    
    for j in s:
        answer += a[(a.find(j) + index) % len(a)]
    return answer