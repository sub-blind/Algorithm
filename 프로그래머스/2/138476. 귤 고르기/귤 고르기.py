from collections import Counter

def solution(k, tangerine):
    answer = 0
    index = 0
    count = Counter(tangerine)
    values = list(count.values())
    
    values.sort(reverse=True)

    while k > 0 and index < len(values):
        k = k - values[index]
        answer = answer + 1
        index = index + 1

    return answer
