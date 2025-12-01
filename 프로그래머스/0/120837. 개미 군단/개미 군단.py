def solution(hp):
    answer = 0
    a = hp // 5
    b = hp % 5 // 3
    c = hp % 5 % 3
    return a + b + c