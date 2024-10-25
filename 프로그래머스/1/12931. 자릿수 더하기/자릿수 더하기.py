def solution(n):
    answer = 0
    lis = list(str(n))
    for i in lis:
        answer += int(i)

    return answer