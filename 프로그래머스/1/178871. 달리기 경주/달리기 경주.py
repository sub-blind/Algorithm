def solution(players, callings):
    rank = {key: i for i, key in enumerate(players)}
    
    for j in callings:
        index = rank[j]
        
        # index가 0이면, 이전 플레이어가 없으므로 넘어감
        if index > 0:
            # 이전 선수와 순위를 변경
            prev_player = players[index - 1]
            # 순위 변경
            rank[players[index - 1]] += 1
            rank[players[index]] -= 1
            # 선수들 교환
            players[index - 1], players[index] = players[index], players[index - 1]
    
    return players
