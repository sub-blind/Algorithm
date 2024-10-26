from collections import Counter

def solution(X, Y):
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    answer = ""
    for digit in range(9, -1, -1):
        str_digit = str(digit)
        
        if str_digit in count_X and str_digit in count_Y:
            answer += str_digit * min(count_X[str_digit], count_Y[str_digit])
    
    if not answer:
        return "-1"
    
    if answer[0] == "0":
        return "0"
    
    return answer
