def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += i
        elif i.islower():
            a = (alpha.index(i) + n) % 26
            answer += alpha[a]
        elif i.isupper():
            a = (alpha.index(i.lower()) + n) % 26
            answer += alpha[a].upper()
            
    return answer