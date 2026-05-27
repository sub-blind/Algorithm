def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score) // m):
        box = score[i*m:(i*m + m)]
        lowest_score = min(box)
        box_price = lowest_score * m
        answer += box_price
        
    return answer