from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = dict(zip(want, number))

    for i in range(len(discount) - 9):
        if Counter(discount[i:i+10]) == dic:
            answer += 1

    return answer