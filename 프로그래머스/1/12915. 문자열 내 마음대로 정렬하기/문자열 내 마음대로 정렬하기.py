def solution(strings, n):
    answer = []
    result = []
    for i in strings:
        answer.append(i[n]+i)
    answer.sort()
    for i in answer:
        result.append(i[1:])
    return result