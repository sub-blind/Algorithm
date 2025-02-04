def solution(n):
    answer = n ** (1/2)
    if answer % 1 == 0:
        return 1
    else:
        return 2